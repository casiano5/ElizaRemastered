const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  pluginOptions: {
    electronBuilder: {
      nodeIntegration: true,
      outputDir: 'dist',
      builderOptions: {
        files: [
          "**/*"
        ],
        extraFiles: [
          {
            "from": "python",
            "to": "python",
            "filter": ["**/*"]
          }
        ],
        appId: "eliza-remastered",
        productName: "Eliza Remastered",
        win: {
          // icon: "path",
        },
        nsis: {
          // installerIcon: "path",
          // uninstallerIcon: "path",
          uninstallDisplayName: "Eliza Remastered",
          license: "LICENSE",
          oneClick: false,
          allowToChangeInstallationDirectory: true
        }
      }
    }
  }
})
