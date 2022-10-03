#!/usr/bin/node

exports.incrementAndcall = function (number, theFunction) {
  theFunction(++number);
};
