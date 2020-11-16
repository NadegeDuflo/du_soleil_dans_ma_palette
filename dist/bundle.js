/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./src/script.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/part_montante.js":
/*!******************************!*\
  !*** ./src/part_montante.js ***!
  \******************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony default export */ __webpack_exports__[\"default\"] = ((function () {\n  var width,\n      height,\n      largeHeader,\n      canvas,\n      ctx,\n      circles,\n      target,\n      animateHeader = true; // Main\n\n  initHeader();\n  addListeners();\n\n  function initHeader() {\n    width = window.innerWidth;\n    height = window.innerHeight;\n    target = {\n      x: 0,\n      y: height\n    };\n    largeHeader = document.getElementById('large-header');\n    largeHeader.style.height = height + 'px';\n    canvas = document.getElementById('demo-canvas');\n    canvas.width = width;\n    canvas.height = height;\n    ctx = canvas.getContext('2d'); // create particles\n\n    circles = [];\n\n    for (var x = 0; x < width * 0.5; x++) {\n      var c = new Circle();\n      circles.push(c);\n    }\n\n    animate();\n  } // Event handling\n\n\n  function addListeners() {\n    window.addEventListener('scroll', scrollCheck);\n    window.addEventListener('resize', resize);\n  }\n\n  function scrollCheck() {\n    if (document.body.scrollTop > height) animateHeader = false;else animateHeader = true;\n  }\n\n  function resize() {\n    width = window.innerWidth;\n    height = window.innerHeight;\n    largeHeader.style.height = height + 'px';\n    canvas.width = width;\n    canvas.height = height;\n  }\n\n  function animate() {\n    if (animateHeader) {\n      ctx.clearRect(0, 0, width, height);\n\n      for (var i in circles) {\n        circles[i].draw();\n      }\n    }\n\n    requestAnimationFrame(animate);\n  } // Canvas manipulation\n\n\n  function Circle() {\n    var _this = this; // constructor\n\n\n    (function () {\n      _this.pos = {};\n      init();\n      console.log(_this);\n    })();\n\n    function init() {\n      _this.pos.x = Math.random() * width;\n      _this.pos.y = height + Math.random() * 100;\n      _this.alpha = 0.1 + Math.random() * 0.3;\n      _this.scale = 0.1 + Math.random() * 0.3;\n      _this.velocity = Math.random();\n    }\n\n    this.draw = function () {\n      if (_this.alpha <= 0) {\n        init();\n      }\n\n      _this.pos.y -= _this.velocity;\n      _this.alpha -= 0.0005;\n      ctx.beginPath();\n      ctx.arc(_this.pos.x, _this.pos.y, _this.scale * 10, 0, 2 * Math.PI, false);\n      ctx.fillStyle = 'rgba(255,255,255,' + _this.alpha + ')';\n      ctx.fill();\n    };\n  }\n})());\n\n//# sourceURL=webpack:///./src/part_montante.js?");

/***/ }),

/***/ "./src/script.js":
/*!***********************!*\
  !*** ./src/script.js ***!
  \***********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _part_montante__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./part_montante */ \"./src/part_montante.js\");\n\nObject(_part_montante__WEBPACK_IMPORTED_MODULE_0__[\"default\"])();\n\n//# sourceURL=webpack:///./src/script.js?");

/***/ })

/******/ });