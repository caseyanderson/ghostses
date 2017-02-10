module.exports = function(grunt) {

  grunt.initConfig({
  pkg: grunt.file.readJSON('package.json'),

  watch: {
    options: {
      livereload: true,
    },
    css: {
      files: ['**/score_generator/css/*.css'],
  },
    html: {
      files: ['**/score_generator/html/*.html'],
    }
  },
  connect: {
    server: {
      options: {
        port: 9000,
        base: '.',
        hostname: '0.0.0.0',
        protocol: 'http',
        livereload: true,
        open: true,
      }
    }
  },
});


grunt.loadNpmTasks('grunt-contrib-watch');
grunt.loadNpmTasks('grunt-contrib-connect');

grunt.registerTask('server', ['connect','watch']);

};

0
