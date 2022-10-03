#!/usr/bin/node

exports.callMeMoby = function (number, theFunction) {
  theFunction(++number);
};
