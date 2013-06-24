  <!doctype html>
 
    <head>
        <meta charset="utf-8">
        <title>RECAP</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">
        <link href="..static/css/bootstrap.css" rel="stylesheet">
        <style type="text/css">
            body{padding-top: 60px;padding-bottom: 40px;}
        </style>
        <link href="http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.3.0/css/bootstrap-responsive.css" rel="stylesheet">
        <!--[if lt IE 9]>
            <script src="http://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.6.1/html5shiv.js"></script>
        <![endif]-->
        
          <meta charset="utf-8" />
  <title>jQuery UI Accordion - Default functionality</title>
  <link rel="stylesheet" href="/static/jquery-ui-1.10.2.custom.min.css.gz" />
  <script src="http://code.jquery.com/jquery-1.9.1.js"></script>
  <script src="http://code.jquery.com/ui/1.10.2/jquery-ui.js"></script>
  
  <script>
  $(function() {
        $( "#accordion" ).accordion({
            collapsible: true,
            active: false,
            heightStyle: "content"
        });
         $("#accordion").css("display", "block");
    });
  </script>
        
        
        
    </head>
  
  <body>
  
 
  <div class="navbar navbar-inverse navbar-fixed-top">
            <div class="navbar-inner">
                <div class="container">
                    <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse"><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span>
                    </button><a class="brand" href="#">RECAP</a>
                    <div class="nav-collapse collapse">
                        <ul class="nav">
                            <li class="active"><a href="/">Start</a>
                            </li>
                            <li><a href="/user_interface">Sales</a>
                            </li>
                            <li><a href="/scoping">Scoping</a>
                            </li>
                            <li><a href="/documentation">Upload</a>
                            </li>
                            </li>
                            <li><a href="/download">Download</a>
                            </li>
                            </li>
                            <li><a href="/logout">logout</a>
                            </li>
                            
                            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
                                <ul class="dropdown-menu">
                                    <li><a href="/map_link">Map Link</a>
                                    </li>
                                    <li><a href="/convertpdf">Create a document(pdf)</a>
                                    </li>
                                    <li><a href="/document">Something else here</a>
                                    </li>
                                    <li class="divider"></li>
                                    <li class="nav-header">Nav header</li>
                                    <li><a href="/scrolling_doc">Scrolling Documents</a>
                                    </li>
                                    <li><a href="/scrolling">Scrolling Introduction</a>
                                    </li>
                        </ul>
                        </li>
                        </ul>
                      
                    </div>
                </div>
            </div>
        </div>
 
 <!-- Le javascript==================================================-->
        <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
        <script src="http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.3.0/js/bootstrap.js"></script>
    </body>
    </html>