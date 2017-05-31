// http://stackoverflow.com/questions/6084360/using-node-js-as-a-simple-web-server
// https://www.npmjs.com/package/node-watch
// https://nodejs.org/api/child_process.html
// https://stackoverflow.com/questions/9781218/how-to-change-node-jss-console-font-color

var control = function(){
    var busy = 0;
    return this;
}();

var clc = require('cli-color');
var watch = require('node-watch');
var moment = require('moment');
const exec = require('child_process').exec;

var run_make = function (control){
    control.busy = 1;
    var now = moment();
    var formatted = now.format('YYYY-MM-DD HH:mm:ss Z');
    console.log("Running make now...");
    console.log(formatted);
//	exec('make clean && make html',
    exec('make html', function (error, stdout, stderr) {
        console.log(clc.blue('OK!'));
        console.warn(clc.yellow(error));
        console.error(clc.red(stderr));
        console.log("Not busy anymore: ", control.busy)
        control.busy = 0;
        console.log("Not busy anymore: ", control.busy)
    });
};

run_make(control);

watch('source', { recursive: true }, function(evt, name) {
    console.log(control.busy);
    if (control.busy == 0) {
        run_make(control);
    }

});


var connect = require('connect');
var serveStatic = require('serve-static');
connect().use(serveStatic("build/html/")).listen(8080, function(){
    console.log('Server running on 8080...');
});

