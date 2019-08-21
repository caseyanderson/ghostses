const gulp = require('gulp');
const sass = require('gulp-sass');
const browserSync = require('browser-sync').create();

// compile scss into css
function style(){
  // find scss file
  return gulp.src('./layer_generator/scss/**/*.scss')
  // pass that file through sass compiler
  .pipe(sass().on('error', sass.logError))
  // where do i save compiled css
  .pipe(gulp.dest('./layer_generator/css/'))
  // stream changes to all browsers
  .pipe(browserSync.stream());
}


// watch for changes in scss or html
function watch(){
  browserSync.init({
    server: {
      baseDir: './layer_generator/',
      directory: true
    }
  });
  gulp.watch('./layer_generator/scss/**/*.scss', style);
  gulp.watch('./layer_generator/html/**/*.html').on('change', browserSync.reload);
}


exports.style = style;
exports.watch = watch;
