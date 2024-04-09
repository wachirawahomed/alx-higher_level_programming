#!/usr/bin/node

exports.esrever = function(list) {
  // Create an empty array to store reversed elements
  let reversedList = [];

  // Iterate over the original list in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    // Add each element to the reversedList array
    reversedList.push(list[i]);
  }

  // Return the reversed list
  return reversedList;
};

