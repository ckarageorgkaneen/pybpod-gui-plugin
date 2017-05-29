// http://stackoverflow.com/questions/6084360/using-node-js-as-a-simple-web-server
// https://www.npmjs.com/package/node-watch
// https://nodejs.org/api/child_process.html
// https://stackoverflow.com/questions/9781218/how-to-change-node-jss-console-font-color

var clc = require('cli-color');
var watch = require('node-watch');
const exec = require('child_process').exec;

watch('source', { recursive: true }, function(evt, name) {
//	exec('make clean && make html',
        exec('make html',

  		function (error, stdout, stderr) {
    		console.log('OK!');
    		console.warn(clc.yellow(error));
    		console.error(clc.red(stderr));
		})
});


var connect = require('connect');
var serveStatic = require('serve-static');
connect().use(serveStatic("build/html/")).listen(8080, function(){
    console.log('Server running on 8080...');
});

