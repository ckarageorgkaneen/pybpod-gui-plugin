// http://stackoverflow.com/questions/6084360/using-node-js-as-a-simple-web-server
// https://www.npmjs.com/package/node-watch
// https://nodejs.org/api/child_process.html
// https://stackoverflow.com/questions/9781218/how-to-change-node-jss-console-font-color

var busy = 0;

var clc = require('cli-color');
var watch = require('node-watch');
var moment = require('moment');
const exec = require('child_process').exec;

var run_make = function (busy){
    busy = 1;
    var now = moment();
    var formatted = now.format('YYYY-MM-DD HH:mm:ss Z');
    console.log("Running make now...");
    console.log(formatted);
//	exec('make clean && make html',
    exec('make html', function (error, stdout, stderr) {
        console.log(clc.blue('OK!'));
        console.warn(clc.yellow(error));
        console.error(clc.red(stderr));
        busy = 0;
    });
};

run_make(busy);

watch('source', { recursive: true }, function(evt, name) {
    console.log(busy);
    if (busy == 0) {
        run_make(busy);
    }

});


var connect = require('connect');
var serveStatic = require('serve-static');
connect().use(serveStatic("build/html/")).listen(8080, function(){
    console.log('Server running on 8080...');
});

