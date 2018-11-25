'use strict';

var os = require('os');
var gulp = require('gulp');
var connect = require('gulp-connect');
var sass = require('gulp-sass');
var open = require('gulp-open');

sass.compiler = require('node-sass');

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


gulp.task('sass', function () {
  return gulp.src('./layer_generator/scss/*.scss')
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(gulp.dest('./layer_generator/css'))
    .pipe(connect.reload());
});

gulp.task('sass:watch', function () {
  gulp.watch('./layer_generator/scss/*.scss', ['sass']);
});


gulp.task('open', function() {
  gulp.src('')
    .pipe(open({uri: 'http://localhost:8080/html/'}));
});

gulp.task('default', ['open', 'connect', 'watch', 'sass:watch']);
