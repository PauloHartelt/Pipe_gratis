# Project Name

Pipe_Gratis

## Description

This project was made to try to answer a question: "How can i make a Data Engineer project, fully automated and on cloud without spending any money or even using a credit card number?"

## Architecture

![image](https://github.com/user-attachments/assets/78b91759-d166-4c67-86d9-f2ee6fb5dada)

## Project Overview

- This is a simple project, my goal was to test some ways to make the extraction, transformation and load on cloud and automated;
- To make this project, i ran teste.py file on PythonAnywhere (https://www.pythonanywhere.com/) for extraction and few transformations, sending the API data to a Google sheets and then, adding this Google sheets to a Big Query sandbox, making the final transformations there;
- I had some limitations for this project. On PythonAnywhere, I couldn't use much of the job's processing power due to a RAM usage limit, so I could only work with small amounts of data. Additionally, there's also a time limit — each extraction can only occur once per day, not hourly or by the minute. On Google Sheets, there's a limitation on the amount of stored data, initially restricted to a thousand rows, although this can be extended. Both BigQuery and PythonAnywhere also have time limitations, where after some time, the application or table is automatically deleted from their systems.    

## Contributors

| [<img src="https://avatars.githubusercontent.com/u/95707984?v=4" width=115><br><sub>Paulo Hartelt</sub>](https://github.com/PauloHartelt) |
| :-----------------------------------------------------------------------------------------------------------------------------: |

## Contact

If you have any questions or suggestions about this project, feel free to contact me through my GitHub profile: [@PauloHartelt](https://github.com/PauloHartelt).
