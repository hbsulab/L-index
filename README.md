# L-index
This repository contains the code and the sample input for outlining leading mutation with L-index.

A. Data Preparation

1. Access the GISAID website and navigate to the "EpiCoV" page. From there, select the "search" tab.
2. Retrieve the "patient status metadata" based on your desired criteria and download the corresponding data.
3. The downloaded file will be in TSV format, containing a list of spike mutations observed in the reported samples. This mutation list serves as the primary input for the L-index algorithm in the deLemus method.

B. Computing L-index Score

1. Download the "deLemus(L-index).py" file provided above and make the necessary modifications to the input parameters as required.
2. For convenience, we have included a sample input in Excel format, which has been preprocessed and prepared in advance.
3. The output file will be generated in Excel format and will consist of the L-index scores assigned to each mutational residue, providing valuable insights into their significance.
4. The corresponding eigen contributions are provided in the same Excel file.
