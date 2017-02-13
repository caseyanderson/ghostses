var gulp = require('gulp');
var connect = require('gulp-connect');
var sass = require('gulp-sass');
var open = require('gulp-open');

var config = {
    port: 9005,
    url: 'http://localhost',
    html: './score_generator/html/*.html',
    css: './score_generator/css/',
    scss: './score_generator/scss/styles.scss',
    base: '/score_generator/html/'
}

var sassOptions = {
    errLogToConsole: true,
    outputStyle: 'expanded'
};

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

gulp.task('open', function(){
    gulp.src('./score_generator/html/')
        .pipe(open({uri: ((config.url).concat(':', config.port, config.base )) }));
});

gulp.task('styles', function() {
    gulp.src(config.scss)
        .pipe(sass(sassOptions).on('error', sass.logError))
        .pipe(gulp.dest(config.css))
        .pipe(connect.reload());
});

gulp.task('watch', function () {
    gulp.watch(config.html, ['html']);
    gulp.watch(config.scss, ['styles']);
});

gulp.task('default', ['connect', 'open', 'watch']);
