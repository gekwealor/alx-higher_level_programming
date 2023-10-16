#!/usr/bin/node

const function = (x, theFunction) => {
  for (; x > 0; x--) {
    theFunction();
  }
};

module.exorts = { callMeMoby };
