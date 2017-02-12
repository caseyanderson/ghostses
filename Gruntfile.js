module.exports = function(grunt) {

  grunt.initConfig({
  pkg: grunt.file.readJSON('package.json'),

  watch: {
    options: {
      livereload: true
    },
    css: {
      files: ['**/score_generator/css/*.css'],
    //   files: ['**/score_generator/scss/*.scss'],
    //   tasks: ['compass']
  },
    html: {
      files: ['**/score_generator/html/*.html']
    }
},
// compass: {
// 			dist: {
// 				options: {
// 					sassDir: 'sass',
// 					cssDir: 'css'
// 				}
// 			}
// 		},
  connect: {
    server: {
      options: {
        port: 9000,
        base: '.',
        hostname: '0.0.0.0',
        protocol: 'http',
        livereload: true,
        open: true
      }
    }
  },
});


grunt.loadNpmTasks('grunt-contrib-watch');
grunt.loadNpmTasks('grunt-contrib-connect');

grunt.registerTask('server', ['connect','watch']);

};
