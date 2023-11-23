declare namespace bun {
  interface Env {
    readonly uid: string;
    readonly token: string;
  }
}

declare namespace NodeJS {
  // 環境変数名の定義
  interface ProcessEnv {
    readonly uid: string;
    readonly token: string;
  }
}
