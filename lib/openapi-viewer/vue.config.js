module.exports = {
  devServer: {
    port: 8080,
    proxy: {
      "/.*/.*": {
        target: "http://localhost:8000",
        ws: true,
        changeOrigin: true,
        logLevel: "debug",
        bypass: function (req) {
          if (
            req.url.endsWith("/ws") ||
            req.url === "javascript/openapi-viewer.min.js"
          ) {
            return req.url;
          }
          return null;
        },
      },
    },
  },

  configureWebpack: {
    output: {
      filename: "javascript/openapi-viewer.min.js",
    },
    optimization: {
      splitChunks: false,
    },
  },

  css: {
    extract: false, // Only if you want to inline CSS in the JavaScript bundle
  },

  productionSourceMap: false,
};
