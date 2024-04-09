import boto3
import requests

# import Types.saveExecutableTypes
# テスト用！！！もうriichi-city-liveで動いてる！！！


def get_latest_version() -> any:
    url = "https://dunu5s1vzgz6j.cloudfront.net/store/webPage"

    headers = {
        "accept": "*/*",
        "accept-language": "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5",
        "content-length": "0",
        "origin": "https://www.mahjong-jp.com",
        "referer": "https://www.mahjong-jp.com/",
        "sec-ch-ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    }

    StoreWebPageResponse = requests.post(url, headers=headers)

    StoreWebPageResponse = StoreWebPageResponse.json()
    # StoreWebPageResponse = Types.saveExecutableTypes.StoreWebPageResponse(**StoreWebPageResponse)
    # json.dumps(StoreWebPageResponse, open("get_latest_version.json", "w"))
    print(StoreWebPageResponse)
    return StoreWebPageResponse


def stream_to_s3(url, bucket, dir, key):
    """
    ストリーミングダウンロードと同時にS3にアップロードする関数。
    """
    print(f"Start Upload {url} to {bucket}/{dir}/{key}")
    s3 = boto3.client("s3")
    response = requests.get(url, stream=True)

    key = f"{dir}/{key}"

    # S3にマルチパートアップロードを開始
    upload_id = s3.create_multipart_upload(Bucket=bucket, Key=key)["UploadId"]
    parts = []

    part_number = 1
    for chunk in response.iter_content(chunk_size=10 * 1024 * 1024):  # 10 MBのチャンク
        print(f"part upload start {part_number}")
        # チャンクをアップロード
        part = s3.upload_part(Bucket=bucket, Key=key, PartNumber=part_number, UploadId=upload_id, Body=chunk)
        parts.append({"PartNumber": part_number, "ETag": part["ETag"]})
        part_number += 1

    # マルチパートアップロードを完了
    s3.complete_multipart_upload(Bucket=bucket, Key=key, UploadId=upload_id, MultipartUpload={"Parts": parts})


def lambda_handler(event, context):
    # DOWNLOAD_URL = "https://d3qgi0t347dz44.cloudfront.net/release/macpack/riichicity_2.1.3_mac_official.zip"
    S3_BUCKET = "executable-playground-dev"
    # OBJECT_KEY = "riichicity_2.1.3_mac_official.zip"

    # stream_to_s3(DOWNLOAD_URL, S3_BUCKET, OBJECT_KEY)
    storeWebPageResponse = get_latest_version()
    if storeWebPageResponse.code != 0:
        return {"statusCode": 500, "body": "Failed to get the latest version."}

    for platform, url in storeWebPageResponse.data.downloadInfo:
        u = url.path.split("/")[-1]
        if u.endswith(".zip") or u.endswith(".dmg") or u.endswith(".exe") or u.endswith(".apk"):
            stream_to_s3(url, S3_BUCKET, platform, u)
            print(f"Uploaded success! {platform}/{u}")

    return {"statusCode": 200, "body": "Upload complete."}


# get_latest_version()
# lambda_handler(None, None)
