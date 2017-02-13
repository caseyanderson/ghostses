var gulp = require('gulp'),
  connect = require('gulp-connect');


  var config = {
      port: 9005,
      url: 'http://localhost',
      html: './score_generator/html/*.html',
      css: './score_generator/css/styles.css',
      scss: './score_generator/scss/styles.scss'
  }

gulp.task('connect', function() {
    connect.server({
        port: config.port,
        base: config.url,
        livereload: true
    });
});

gulp.task('html', function () {
    gulp.src(config.html)
    .pipe(connect.reload());
});

gulp.task('watch', function () {
    gulp.watch(config.html, ['html']);
});

gulp.task('default', ['connect', 'watch']);
