# Sekoia.io OpenAPI Viewer library

This viewer library is a Sekoia.io custom instrumentation of [Redoc](https://github.com/Redocly/redoc), providing
* easier navigation in a large API doc using OpenAPI 3.1 tags and tagGroups
* client-side merging of several OpenAPI/Swagger manifests
* hosting region selector
* plans and permissions handling
* in-browser try-it editor

Any update to this library's code should be **compiled before commit**.
The compiled library [../openapi-viewer.js](../openapi-viewer.js) is versioned and pushed to this repo to keep our Documentation repo dependency-free.

If you need to modify the library's code please run
```bash
yarn
yarn build
```
to compile [../openapi-viewer.js](../openapi-viewer.js)

For best DX, you may use the webpack devserver via
```bash
yarn
yarn start
```