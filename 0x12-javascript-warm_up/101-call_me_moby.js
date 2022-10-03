#!/usr/bin/node

exports.excuteXtimes = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
