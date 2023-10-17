#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return (list.filter(data => data === searchElement).length);
};
