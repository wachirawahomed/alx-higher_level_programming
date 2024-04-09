#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destinationFile = process.argv[4];

// Read contents of fileA
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    return;
  }
  
  // Read contents of fileB
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      return;
    }
    
    // Concatenate contents of fileA and fileB
    const concatenatedData = dataA + dataB;
    
    // Write concatenated data to the destination file
    fs.writeFile(destinationFile, concatenatedData, (err) => {
      if (err) {
        console.error(err);
        return;
      }
      
      console.log(`Concatenation of ${fileA} and ${fileB} saved to ${destinationFile}`);
    });
  });
});

