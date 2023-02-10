exports.factorial = function(num) {

  let x = 1
  for(let i = 1; i <= num; i++){
    x = x * i
  }
  return x 
};
