'use strict';

var os = require('os');
var gulp = require('gulp');
var  connect = require('gulp-connect');

gulp.task('connect', function() {
  connect.server({
    root: 'score_generator',
    livereload: true
  });
});

gulp.task('html', function () {
  gulp.src('./score_generator/html/*.html')
    .pipe(gulp.dest('./score_generator/html/'))
    .pipe(connect.reload());
});

gulp.task('watch', function () {
  gulp.watch(['./score_generator/html/*.html'], ['html']);
});

gulp.task('default', ['connect', 'watch']);
