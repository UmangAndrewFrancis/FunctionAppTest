import requests
import logging
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        import pandas
        wsdl = 'http://google.com'
        # headers = {'content-type': 'text/xml'}

        # body = """
        # <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:exam="http://www.example.org">
        #     <soapenv:Header/>
        #     <soapenv:Body>
        #         <exam:process>
        #             <exam:RECORD_DATE>10-JAN-2020</exam:RECORD_DATE>
        #         </exam:process>
        #     </soapenv:Body>
        # </soapenv:Envelope>
        # """

        response = requests.get(wsdl)
        logging.info(response)
        print(response.content)
        logging.info('Successful')
        return func.HttpResponse(
            "No Error"
        )
    except Exception as e:
        return func.HttpResponse(
            "Error: "+str(e),
            status_code=400
        )
