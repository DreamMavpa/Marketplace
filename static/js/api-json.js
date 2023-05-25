function get_json_id(modal_content_id){ 
    let filter_data = modal_content_id.replaceAll('&#39;',''); 
    let info_product_arr = filter_data.split(',');
	block_creator(info_product_arr[0],info_product_arr[1],info_product_arr[2],info_product_arr[3],info_product_arr[4]);
};

