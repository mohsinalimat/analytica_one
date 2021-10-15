// Copyright (c) 2021, THE ELECTRONIC COMMERCE & DATA CONSULTANTS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Forecast Settings', {
	/*validate: function(frm) {
		console.log('validate');
		for(var i=0;i<frm.doc.supplier_forecast.length;i++){
			var a = frm.doc.supplier_forecast[i].ksa_central;
			var b = frm.doc.supplier_forecast[i].ksa_ea_hpi;
			var c = frm.doc.supplier_forecast[i].ksa_western;
			var d = frm.doc.supplier_forecast[i].ksa_aramco;
			var e = frm.doc.supplier_forecast[i].ksa_service;
			var g = frm.doc.supplier_forecast[i].qatar;
			var h = frm.doc.supplier_forecast[i].jordan;
			var j = frm.doc.supplier_forecast[i].bahrain;
			var total = parseFloat(a) + parseFloat(b) + parseFloat(c) + parseFloat(d) + parseFloat(e);
			console.log(total);
			var tot_k = parseFloat(a) + parseFloat(b) + parseFloat(c) + parseFloat(d) + parseFloat(e) + parseFloat[g] + parseFloat[h] + parseFloat[j];
			console.log(tot_k);
			frm.doc.supplier_forecast[i].total_value_ksa = total;
			frm.doc.supplier_forecast[i].target = tot_k;
		}

	}*/
});
frappe.ui.form.on('Supplier Forecast', {
	validate: function(frm){
		console.log('called validate');
		var child = locals[cdt][cdn];
		var a = child.ksa_central;
		var b = child.ksa_ea_hpi;
		var c = child.ksa_western;
		var d = child.ksa_aramco;
		var e = child.ksa_service;
		var total = parseFloat(a) + parseFloat(b) + parseFloat(c) + parseFloat(d) + parseFloat(e);
		console.log(total);
		child.total_value_ksa = total;
		console.log(child.total_value_ksa);
		cur_frm.refresh_fields();
	}
});