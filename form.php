<?php
    
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
          
        function get_data() {
            $datae = array();
            $datae[] = array(
                'Gender' => $_POST['gen'],
                'Ethnicity' => $_POST['ethn'],
                'Jaundice' => $_POST['jaun'],
                'Country' => $_POST['coun'],
                'Q1' => $_POST['q1'],
                'Q2' => $_POST['q2'],
                'Q3' => $_POST['q3'],
                'Q4' => $_POST['q4'],
                'Q5' => $_POST['q5'],
                'Q6' => $_POST['q6'],
                'Q7' => $_POST['q7'],
                'Q8' => $_POST['q8'],
                'Q9' => $_POST['q9'],
                'Q10' => $_POST['q10'],
                
            );
            return json_encode($datae);
        }
          
        $name = "data";
        $file_name = $name . '.json';
       
        if(file_put_contents(
            "$file_name", get_data())) {
                echo $file_name .' file created';
            }
        else {
            echo 'There is some error';
        }
    }
?>