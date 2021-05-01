
const imgLinks = [
  'image/book6.jpg',
  'image/book5.jpg',
];
const delay = 5000;
let currentIndex = 0;
setInterval(function() {
  document.getElementById('image').src = imgLinks[currentIndex];
  currentIndex++;
  if(currentIndex >= imgLinks.length) {
      currentIndex = 0;
  }
}, delay);

