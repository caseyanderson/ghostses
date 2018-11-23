'use strict';

var os = require('os');
var gulp = require('gulp');
var  connect = require('gulp-connect');

gulp.task('connect', function() {
  connect.server({
    root: 'layer_generator',
    livereload: true
  });
});

gulp.task('html', function () {
  gulp.src('./layer_generator/html/*.html')
    .pipe(gulp.dest('./layer_generator/html/'))
    .pipe(connect.reload());
});

gulp.task('watch', function () {
  gulp.watch(['./layer_generator/html/*.html'], ['html']);
});

gulp.task('default', ['connect', 'watch']);
