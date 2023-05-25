async function get_modal_id_js(modal_content_id, dir_name, db) {
  try {
    const response = await fetch('/api');
    const data = await response.json();
    json_generate_block(data[db], modal_content_id, dir_name, db);
  } catch (error) {
    console.log(error);
  }
}

function json_generate_block(json_img, modal_content_id, dir_name, db) {

  const len_js_img = json_img[modal_content_id].length;
  const app = document.querySelector('.product-pictures');
  const popUpImgScroll = document.querySelector(".big-block-img")
  let get_group_img_block = '';
  let get_group_img_block_popUp = '';
  const div = document.createElement('div');
  div.className = 'swiper-slide';

  for (let i = 0; i < len_js_img; i++) {

    const imgPath = `/static/img/img_shop/${dir_name}/${modal_content_id}/img/${json_img[modal_content_id][i]}`;
    get_group_img_block += `<div class="product-picture zzz" id=${i} style="background: center url('${imgPath}'); background-size: cover;"></div>`;
    get_group_img_block_popUp += `<div class="zxc" id=${i} style="background: center url('${imgPath}'); background-size: cover;"></div>`;
    // get_group_img_block += `<div class="product-picture" style="background: center url('${imgPath}'); background-size: cover;"></div>`;
    
  }

  app.insertAdjacentHTML('afterbegin', get_group_img_block);
  popUpImgScroll.insertAdjacentHTML('afterbegin', get_group_img_block_popUp);
}
  

async function btn_drop_json() {
  let cart = JSON.parse(localStorage.getItem('cart')) || [];

  if (document.querySelector("#cart_name").value == ''){
    alert('Заполните поле ФИО!')
  }
  else if (document.querySelector("#cart_tel").value.length == '' ){
    alert('Заполните поле номер телефона!')
  }

  else if (document.querySelector("#cart_tel").value.length != 15 ){
    alert('Номер телефона введен не полностью!')
  }

  else{
    
        cart.push({
          name : document.querySelector("#cart_name").value,
          email : document.querySelector("#cart_email").value,
          tel : document.querySelector("#cart_tel").value,
          shippingAddress : document.querySelector("#cart_address").value,
          comment: document.querySelector("#cart_comment").value,
        })
       
        let drop_json_dict = JSON.stringify(cart);
        try {
          await fetch('http://127.0.0.1:5000/jsondrop', {
            method: 'POST',
            body: drop_json_dict,
          });
        } catch (error) {
          console.log(error);
        }
      }
}


window.addEventListener("load", function() {
  let picture_future = document.querySelector(".product-picture-future")
  let firstPic = /url\(['"]?([^'"]+)['"]?\)/.exec(document.querySelector(".product-picture").style.background)[1]
  picture_future.style.background = `url(${firstPic})  no-repeat center center / cover padding-box content-box`

  let allPics = document.querySelectorAll(".product-picture")
  allPics.forEach((e, i) => {
    e.addEventListener("click", () => {
      picture_future.style.background = `url(${/url\(['"]?([^'"]+)['"]?\)/.exec(e.style.background)[1]}) no-repeat center center / cover padding-box content-box`
    
      picture_future.id = event.target.id;
    

    })
  })



  let SizeSelect = document.querySelector("select#SizeSelect")
  let GridSize = document.querySelector("select#GridSize")
  let assembly = document.querySelector("select#assembly")
  let legs = document.querySelector("select#legs")

  SizeSelect.addEventListener("change", () => {

    let productPrice = document.querySelector(".product-price")
    productPrice.innerText = `${Number(SizeSelect.value) + Number(GridSize.value) + Number(assembly.value) + Number(legs.value)}  pуб.` 
  })
  
  GridSize.addEventListener("change", () => {
  
    let productPrice = document.querySelector(".product-price")
    productPrice.innerText = `${Number(SizeSelect.value) + Number(GridSize.value) + Number(assembly.value) + Number(legs.value)}  pуб.` 
  })
  
  assembly.addEventListener("change", () => {

    let productPrice = document.querySelector(".product-price")
    productPrice.innerText = `${Number(SizeSelect.value) + Number(GridSize.value) + Number(assembly.value) + Number(legs.value)}  pуб.` 
  })

  legs.addEventListener("change", () => {
    
    let productPrice = document.querySelector(".product-price")
    productPrice.innerText = `${Number(SizeSelect.value) + Number(GridSize.value) + Number(assembly.value) + Number(legs.value)}  pуб.` 
  })





  
});









function btnSubmit()
{
  
  
  let imgBtn =  document.querySelector(".product-picture-future");
  const contactsPopUp = document.querySelector(".big-block-img-wrapper");
  const popUpImgScroll = document.querySelector(".big-block-img");
  var body = document.getElementsByTagName('body')[0];
  const btnNextDisplay = document.querySelector(".btn-carousel-next")
  const btnPrevDisplay = document.querySelector(".btn-carousel-prev")
  imgBtn.addEventListener('click', () => {
      contactsPopUp.classList.remove("popUphidden")
      contactsPopUp.classList.add("popUpshown")
  
      let clonedElement = imgBtn.cloneNode(true);
  
    
      btnNextDisplay.style.display = "block";
      btnPrevDisplay.style.display = "block";
      clonedElement.className = "zxc";
      // popUpImgScroll.appendChild(clonedElement)
      body.style.overflow = 'hidden';
  
      document.body.scrollTop = 0; 
      document.documentElement.scrollTop = 0;





contactsPopUp.addEventListener("click", () => {
    btnNextDisplay.style.display = "none";
    btnPrevDisplay.style.display = "none";
    contactsPopUp.classList.remove("popUpshown")
    contactsPopUp.classList.add("popUphidden")
    // popUpImgScroll.innerHTML = ''
    body.style.overflow = 'visible';
  })


    

 
  
  
const carousel = document.querySelector('.big-block-img');
const prevBtn = document.querySelector('#prevBtn');
const nextBtn = document.querySelector('#nextBtn');

let currentIndex = parseInt(imgBtn.id); // начальный индекс изображения

function moveToIndex(index) {
  carousel.scrollLeft = carousel.offsetWidth * index;
}

// перемещение к новому индексу при загрузке страницы
moveToIndex(currentIndex);

prevBtn.addEventListener('click', () => {
  if (currentIndex > 0) {
    currentIndex--;
  
    moveToIndex(currentIndex);
  }
});

nextBtn.addEventListener('click', () => {
  if (currentIndex < carousel.children.length - 1) {      
    currentIndex++;
    
    moveToIndex(currentIndex);
  }
});





  });
  
  
}
  
  
  