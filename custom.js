if($(IPython.toolbar.selector.concat(' > #AIedu')).length == 0) {
  IPython.toolbar.add_buttons_group([{
    'label'   : 'AIedu',
    'icon'    : 'fa fa-angle-double-down',
    'callback': function() {
  var cell=IPython.notebook.get_selected_cell();
      cell.set_text('%matplotlib inline\nfrom aiedu import home\nhome.init()');
      IPython.notebook.execute_cell(cell);
    }}], 'AIedu');}

function launch_first_cell (evt) {
  //alert(evt.type);
  if (!launch_first_cell.executed
      //&& evt.type=='kernel_ready'	
      && IPython.notebook.kernel 
      && IPython.notebook.kernel.is_connected()
     ) {
      var codeBlock = '%matplotlib inline\nfrom aiedu import home\nhome.init()';
      //var cellTop=IPython.notebook.get_selected_cell();
      //var cellTop = IPython.notebook.insert_cell_above('code', 0);
      var cellTop = IPython.notebook.get_cells()[0];
      if (cellTop.get_text().length >0 && cellTop.get_text() != codeBlock) {
	  cellTop = IPython.notebook.insert_cell_above('code', 0).set_text(codeBlock);
	  IPython.notebook.get_cells()[0].execute();
      } else if (cellTop.get_text().length >0 && cellTop.get_text() == codeBlock) {
	  //cellNew = IPython.notebook.insert_cell_below('code');
	  //cellNew.set_text(codeBlock);
	  //IPython.notebook.get_cells()[0].execute();
      } else {
	  cellTop.set_text(codeBlock);
	  //IPython.notebook.get_cells()[0].execute();
      }
      //cellTop.set_text(codeBlock);
      //cellTop.clear_output();
      //IPython.notebook.execute_cell(cellTop);
      //IPython.notebook.get_cells()[0].execute();
      launch_first_cell.executed = true;
  }
  IPython.notebook.get_cells()[0].execute();

  return launch_first_cell;
}

$([IPython.events]).on('kernel_ready.Kernel kernel_created.Session', launch_first_cell);


define([
        'base/js/namespace',
        'base/js/promises'
     ], function(Jupyter, promises) {
         promises.notebook_loaded.then(function(appname) {
	     //alert('notebook loaded');
             //if (appname === 'Notebook') {
             //    alert('notebook loaded');
             //}
         });
         promises.checkpoint_restored.then(function(appname) {
	     //alert('checkpoint restored');
             //if (appname === 'Notebook') {
             //    alert('notebook loaded');
             //}
         });
     });
