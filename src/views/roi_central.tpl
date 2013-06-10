<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>jQuery UI Accordion - Collapse content</title>
  <link rel="stylesheet" href="http://code.jquery.com/ui/1.10.0/themes/base/jquery-ui.css" />
  <script src="http://code.jquery.com/jquery-1.8.3.js"></script>
  <script src="http://code.jquery.com/ui/1.10.0/jquery-ui.js"></script>
  <link rel="stylesheet" href="/resources/demos/style.css" />
  <script>
  $(function() {
    $( "#accordion" ).accordion({
      collapsible: true
    });
  });
  </script>
</head>
<body>
 
<div id="accordion">
  <h3>ROI1</h3>
  <div>
  
  %include roi roi_holder = roi_holder
  
  
  </div>
  <h3>ROI 2</h3>
  <div>

%include roi_list

  </div>
  <h3>ROI 3</h3>
  <div>
    %include roi_recalculate roi_holder = roi_holder
  </div>
  
</div>
 
 
</body>
</html>