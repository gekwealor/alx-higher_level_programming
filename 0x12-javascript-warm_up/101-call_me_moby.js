#!/usr/bin/node

const CallMeMoby = (x, theFunction) => {
  for (; x > 0; x--) {
    theFunction();
  }
};

module.exorts = { callMeMoby };
