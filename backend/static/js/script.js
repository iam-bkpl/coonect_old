$(document).ready(function() {
    $('.toggle-button').click(function() {
      $('.navbar').toggleClass('active');
    });
  });
  
// let searchForm = document.querySelector('.search-form');

// document.querySelector('#search-btn').onclick = () =>{
//     searchForm.classList.toggle('active');
//     shoppingCart.classList.remove('active');
//     loginForm.classList.remove('active');
//     navbar.classList.remove('active');
// }

// let shoppingCart = document.querySelector('.shopping-cart');

// document.querySelector('#cart-btn').onclick = () =>{
//     shoppingCart.classList.toggle('active');
//     searchForm.classList.remove('active');
//     loginForm.classList.remove('active');
//     navbar.classList.remove('active');
// }

// let loginForm = document.querySelector('.login-form');

// document.querySelector('#login-btn').onclick = () =>{
//     loginForm.classList.toggle('active');
//     searchForm.classList.remove('active');
//     shoppingCart.classList.remove('active');
//     navbar.classList.remove('active');
// }

// let navbar = document.querySelector('.navbar');

// document.querySelector('#menu-btn').onclick = () =>{
//     navbar.classList.toggle('active');
//     searchForm.classList.remove('active');
//     shoppingCart.classList.remove('active');
//     loginForm.classList.remove('active');
// }

// window.onscroll = () =>{
//     searchForm.classList.remove('active');
//     shoppingCart.classList.remove('active');
//     loginForm.classList.remove('active');
//     navbar.classList.remove('active');
// }

// var swiper = new Swiper(".product-slider", {
//     loop:true,
//     spaceBetween: 20,
//     autoplay: {
//         delay: 7500,
//         disableOnInteraction: false,
//     },
//     centeredSlides: true,
//     breakpoints: {
//       0: {
//         slidesPerView: 1,
//       },
//       768: {
//         slidesPerView: 2,
//       },
//       1020: {
//         slidesPerView: 3,
//       },
//     },
// });

// var swiper = new Swiper(".review-slider", {
//     loop:true,
//     spaceBetween: 20,
//     autoplay: {
//         delay: 7500,
//         disableOnInteraction: false,
//     },
//     centeredSlides: true,
//     breakpoints: {
//       0: {
//         slidesPerView: 1,
//       },
//       768: {
//         slidesPerView: 2,
//       },
//       1020: {
//         slidesPerView: 3,
//       },
//     },
// });
// **************Slider JS*************

// var slides=document.querySelector('.slider-items').children;
// var nextSlide=document.querySelector(".right-slide");
// var prevSlide=document.querySelector(".left-slide");
// var totalSlides=slides.length;
// var index=0;

// nextSlide.onclick=function () {
//     next("next");
// }
// prevSlide.onclick=function () {
//     next("prev");
// }

// function next(direction){

//   if(direction=="next"){
//      index++;
//       if(index==totalSlides){
//        index=0;
//       }
//   } 
//   else{
//           if(index==0){
//            index=totalSlides-1;
//           }
//           else{
//            index--;
//           }
//    }

//  for(i=0;i<slides.length;i++){
//          slides[i].classList.remove("active");
//  }
//  slides[index].classList.add("active");     

// }


// // ***************For Auto Slider*******************
// function first() {
//     document.getElementById("slide-image").src = "image/roomSlider2.jpg";
// }
// function second() {
//     document.getElementById("slide-image").src = "image/roomSlider3.jpg";
// }
// function third() {
//     document.getElementById("slide-image").src = "image/roomSlider4.jpg";
// }
// function fourth() {
//     document.getElementById("slide-image").src = "image/roomSlider1.jpg";
// }
// setInterval(first,2000);
// setInterval(second,4000);
// setInterval(third,6000);
// setInterval(fourth,8000);





