  <!doctype html>
 
    <head>
        <meta charset="utf-8">
        <title>RECAP</title>
        <META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
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
  

  <div class="navbar navbar-inverse navbar-fixed-top" >
  
             <div class="navbar-inner" >
            
             
             
                <div class="container">
                
                
                
                    <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse"><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span>
                    </button><a class="brand" href="#">Recap for {{username}}</a>
                    <div class="nav-collapse collapse">
                        <ul class="nav">
                            <li><a href="/">Introduction<i class="icon-book icon-white"></i></a>
                            </li>
                            <li><a href="/user_interface">Sales<i class="icon-home icon-white"></i></a>
                            </li>
                            <li><a href="/scoping">Scoping<i class="icon-eye-open icon-white"></i></a>
                            </li>
                            
                            <li><a href="/map_link">MAP<i class="icon-search icon-white"></i></a>
                                    </li>
                            
                            <li class="dropdown " ><a href="#" class="dropdown-toggle" data-toggle="dropdown">More<b class="caret"></b></a>
                                <ul class="dropdown-menu">
                                    
                                    <li><a href="/download">Download<i class="icon-envelope "></i></a>
                            		</li>                                    
                                    <li><a href="/convertpdf">Create a document(pdf)<i class="icon-file "></i></a>
                                    </li>                                   
                                 
                                    <li class="divider"></li>
                                    
                                    <li class="nav-header">Others</li>
                                    <li><a href="/scrolling_doc">Answers<i class="icon-pencil "></i></a>
                                    </li>   
                                    <li><a href="/unanswered">Unanswered<i class="icon-edit "></i></a>
                                    </li.
                                    <li><a href="/scrolling">Scrolling Introduction<i class="icon-certificate"></i></a>
                                    </li>
                                    </li>
                            		<li><a href="/welcome">Welcome Page<i class="icon-refresh"></i></a>
                        			</li>
                        			
                           		<li><a href="javascript:window.print()">Print this page<i class="icon-print"></i></a>
                         			</li>
                                    </ul>
                        	</li>
                        
                        
                        
                            <li><a href="/logout">Logout</a>
                         	</li>
                           <li><a href="javascript:window.print()"><img src="/static/image/click-here-to-print.jpg" alt="print this page" id="print-button" height="30" width="100"/></a>

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