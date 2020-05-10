const path = require('path');
const webpackPlugin = require('copy-webpack-plugin');

module.exports = {
  pages: {
    index: {
      entry: 'frontend/src/main.js',
      template: 'frontend/public/index.html',
    },
  },
  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'frontend/src'),
      },
    },
  },
  chainWebpack: (config) => {
    config
      .plugin('copy')
      .use(webpackPlugin, [[{
        from: path.resolve(__dirname, 'frontend/public'),
        to: path.resolve(__dirname, 'dist'),
        toType: 'dir',
        ignore: ['.DS_Store'],
      }]]);
  },
};
