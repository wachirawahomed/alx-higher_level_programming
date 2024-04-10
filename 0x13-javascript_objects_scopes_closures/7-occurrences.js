#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Count the number of occurrences of searchElement in list
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};

