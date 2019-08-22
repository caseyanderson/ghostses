const gulp = require('gulp');
const sass = require('gulp-sass');
const postcss = require("gulp-postcss");
const autoprefixer = require("autoprefixer");
const cssnano = require("cssnano");
const browserSync = require('browser-sync').create();


// paths to scss, html files
var paths = {
  styles: {
    src: "./layer_generator/scss/**/*.scss",
    dest: "./layer_generator/css/"
  },
  html: {
    src:"./layer_generator/html/**/*.html"
  }
};


// compile scss into css
function style(){
  return gulp.src(paths.styles.src)
  .pipe(sass().on('error', sass.logError))
  .pipe(postcss([autoprefixer(), cssnano()]))
  .pipe(gulp.dest(paths.styles.dest))
  // stream changes to all browsers
  .pipe(browserSync.stream());
}


// watch for changes in scss or html
function watch(){
  browserSync.init({
    server: {
      baseDir: "./layer_generator/",
      directory: true
    }
  });
  gulp.watch(paths.styles.src, style);
  gulp.watch(paths.html.src).on('change', browserSync.reload);
}


exports.style = style;
exports.watch = watch;
