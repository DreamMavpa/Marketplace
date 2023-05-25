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
    console.log(json_img);
    const len_js_img = json_img[1].length;
    const app = document.querySelector('.product-pictures-block');
    let get_group_img_block = '';
    const div = document.createElement('div');
    div.className = 'swiper-slide';
  
    for (let i = 0; i < len_js_img; i++) {
      console.log(modal_content_id);
      const imgPath = `/static/img/img_shop/${dir_name}/${modal_content_id}/img/${json_img[modal_content_id][i]}`;
      get_group_img_block += `<div class="product-picture" style="background: center url('${imgPath}'); background-size: cover;"></div>`;
      console.log(`http://127.0.0.1:5000/product-modal/3${imgPath}`);
    }
  
    app.insertAdjacentHTML('afterbegin', get_group_img_block);
  }
  
  async function btn_drop_json() {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    
  
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
  


window.addEventListener("load", function() {
    let SizeSelect = document.querySelector("select#SizeSelect")
    SizeSelect.addEventListener("change", () => {
        let productPrice = document.querySelector(".product-price")
        productPrice.innerText = `${SizeSelect.value} p.`
    })
});


