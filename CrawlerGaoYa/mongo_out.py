from pymongo import MongoClient
from bson.objectid import ObjectId
import json


def court_shixin_out():
    conn = MongoClient()
    collection = conn.crawler_gaoya.court_shixin

    f = open('court_shixin.log', 'w', encoding='utf-8')
    f.write('name,identityNumber,dsSign,grabTime,isHit,hitNum,loseCreditDetail\n')

    for item in collection.find(no_cursor_timeout=True):
        identifications = item.get('identifications')
        try:
            if identifications:
                name = identifications.get('name'),
                identityNumber = identifications.get('identityNumber'),
                dsSign = 'https://www.baidu.com',
                grabTime = identifications.get('grabTime'),
                # isSuccess = identifications.get(''),
                # failReason = identifications.get(''),
                isHit = identifications.get('isHit', False) or False,
                hitNum = identifications.get('hitNum', 0),
                loseCreditDetail = identifications.get('loseCreditDetail')

                line = ','.join([i.replace('[', '').replace(']', '') for i in
                                 list(map(json.dumps,
                                          (name, identityNumber, dsSign, grabTime, isHit, hitNum, loseCreditDetail)))])

                f.write(line + '\n')
                print('new line: ', line)
        except Exception as e:
            print('error: ', e)

    f.close()
    print('down!')


def society_credit_check_out():
    conn = MongoClient()
    collection = conn.crawler_gaoya.society_credit_check

    # for item in collection.find({'_id': ObjectId('59c235e45ab35948e8d2f283')}):
    #     print('item: ', item)
    #     search_company_name = item.get('search_company_name')
    #     isHit = False
    #     societyCreditDetail = {}
    #     content = item.get('content')
    #
    #     if content:
    #         try:
    #             content = json.loads(content)
    #         except:
    #             content = ''
    #
    #     try:
    #         detail = content[1][0]
    #         if detail:
    #             isHit = True
    #             societyCreditDetail['unifiedSocialCreditCode'] = detail.get('tydm')
    #             societyCreditDetail['organizationNames'] = detail.get('jgmc')
    #             societyCreditDetail['registrationNumber'] = detail.get('zch')
    #             societyCreditDetail['registerDate'] = detail.get('zcrq')
    #             societyCreditDetail['expirationDate'] = detail.get('zfrq')
    #
    #
    #             print('new line111: ', societyCreditDetail)
    #         else:
    #             print('new line222: ', societyCreditDetail)
    #     except Exception as e:
    #         print('new line333: ', societyCreditDetail)

    f = open('society_credit_check_out.log', 'w', encoding='utf-8')
    f.write('search_company_name,isHit,societyCreditDetail\n')

    for item in collection.find(no_cursor_timeout=True):
        search_company_name = item.get('search_company_name')
        isHit = False
        societyCreditDetail = {}
        content = item.get('content')

        if content:
            try:
                content = json.loads(content)
            except:
                content = ''

        try:
            detail = content[1][0]
            if detail:
                isHit = True
                societyCreditDetail['unifiedSocialCreditCode'] = detail.get('tydm')
                societyCreditDetail['organizationNames'] = detail.get('jgmc')
                societyCreditDetail['registrationNumber'] = detail.get('zch')
                societyCreditDetail['registerDate'] = detail.get('zcrq')
                societyCreditDetail['expirationDate'] = detail.get('zfrq')

                line = ','.join([i.replace('[', '').replace(']', '') for i in
                                 list(map(json.dumps, (search_company_name, isHit, societyCreditDetail)))])

                f.write(line + '\n')
                print('new line111: ', line)
            else:
                line = ','.join([i.replace('[', '').replace(']', '') for i in
                                 list(map(json.dumps, (search_company_name, isHit, societyCreditDetail)))])
                f.write(line + '\n')
                print('new line222: ', line)
        except Exception as e:
            line = ','.join([i.replace('[', '').replace(']', '') for i in
                             list(map(json.dumps, (search_company_name, isHit, societyCreditDetail)))])
            f.write(line + '\n')
            print('new line333: ', line)

    f.close()
    print('down!')


def society_credit_check_result_out():
    conn = MongoClient()
    collection = conn.crawler_gaoya.society_credit_check_result

    f = open('society_credit_check_result.log', 'w', encoding='utf-8')
    f.write('search_company_name,organizationName,unifiedSocialCreditCode,issue\n')

    for item in collection.find(no_cursor_timeout=True):
        search_company_name = item.get('search_company_name', '')
        organizationName = item.get('JGMC', '')
        unifiedSocialCreditCode = item.get('TYSHXYDM', '')
        issue = item.get('EFLAG', '')

        line = ','.join([i.replace('[', '').replace(']', '') for i in
                         list(map(json.dumps,
                                  (search_company_name, organizationName, unifiedSocialCreditCode, issue)))])

        f.write(line + '\n')
        print('new line: ', line)

    f.close()
    print('down!')

if __name__ == '__main__':
    society_credit_check_result_out()
