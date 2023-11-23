export interface Passport {
  accessToken: string;
  uid: string;
}

export interface VersionResponse {
  version: string; // "0.10.302.w",
  force_version: string; //"0.10.0.w",
  code: string; // "v0.10.302.w/code.js"
}

const JP_HOST = "https://game.mahjongsoul.com";
const PASSPORT_HOST = "https://passport.mahjongsoul.com/";
async function setup() {
  const passport = await fetch(`${JP_HOST}/version.json`, {
    headers: {
      accept: "application/json, text/plain, /",
      "content-type": "application/json;charset=UTF-8",
      "sec-ch-ua":
        '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": '"Windows"',
      Referer: "https://game.mahjongsoul.com/",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    },
    method: "GET",
  });
  const json = (await passport.json()) as VersionResponse;
  console.log(json);
}
type ConfigResponse = {
  ip: {
    name: string;
    region_urls: {
      url: string;
      ob_url: string;
    }[];
  }[];
  goods_sheleve_id: string;
  yo_service_url: string[];
  yo_sdk_js: string;
  jp_shop_js: string;
  jp_shop_id: string;
};
async function config(version: string) {
  const headers = {
    headers: {
      accept: "application/json, text/plain, /",
      "content-type": "application/json;charset=UTF-8",
      "sec-ch-ua":
        '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": '"Windows"',
      Referer: "https://game.mahjongsoul.com/",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    },
    method: "GET",
  };
  const configRes = await fetch(`${JP_HOST}/v${version}/config.json`, headers);
  const json = (await configRes.json()) as ConfigResponse;
  const url = json.ip[0].region_urls[0].url;
  const passport_url = json.yo_service_url[0];
  console.log(passport_url);
  console.log(url);
  console.log(json);
  const getWebSocketServerRes = await fetch(
    url + "?service=ws-gateway&protocol=ws&ssl=true",
    headers
  );
  const json2 = await getWebSocketServerRes.json();
  console.log(json2);
}

async function main() {
  const passport = await fetch("https://passport.mahjongsoul.com/user/login", {
    headers: {
      accept: "application/json, text/plain, /",
      "content-type": "application/json;charset=UTF-8",
      "sec-ch-ua":
        '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": '"Windows"',
      Referer: "https://game.mahjongsoul.com/",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    },
    body: '{"uid":"44291295","token":"455bdebe50fb434b90a81b90f1f5d030","deviceId":"web|44291295"}',
    method: "POST",
  });
  const json = await passport.json();
  console.log(json);
}
// main();
// setup();
await config("0.10.302.w");
