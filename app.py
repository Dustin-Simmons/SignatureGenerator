from flask import Flask, render_template, request, url_for, redirect
from secure import Secure

# Create app, set csrf key, and activate security.py
app = Flask(__name__)
secure = Secure()

# Store address dictionary
store_dict = {
    '100 Park City': '1664 Uinta Way #C-2/Park City, UT 84098',
    '101 Orem': '775 E University Parkway/Orem, UT 84097',
    '102 Ft. Union': '6936 South Park Center Drive/Cottonwood Heights, UT 84121',
    '105 St. George': '473 South River Road, Suite 2/St. George, UT 84790',
    '106 Foothill': '1414 Foothill Drive Suite A-2/Salt Lake City, UT 84108',
    '200 Lubbock': '2407 9th Street, Suite 200/Lubbock, TX 79401',
    '203 Tyler': '4919 S. Broadway Avenue/Tyler, TX 75703',
    '205 Rogers': '2603 W Pleasant Grove Rd, Suite 103/Rogers, AR 72758',
    '206 Katy': '23730 Westheimer Parkway, Space 730-T/Katy, TX 77494',
    '207 Waco': '300 S. 2nd Street, Suite 104/Waco, TX 76701',
    #'208 San Marcos': '200 Springtown Way, Suite 122/San Marcos, TX 78666',
    '301 Evansville': '6401 E Lloyd Expressway, Suite 17/Evansville, IN 47715',
    '305 Ft. Wayne': '4130 W Jefferson Blvd, Suite I-7/Fort Wayne, IN 46804',
    '308 Cincinnati': '7532 Gibson St., Space E-108/Cincinnati, OH 45069',
    '312 Nashville': '2018 Lindell Avenue/Nashville, TN 37203',
    '313 Vanderbilt': '2509 West End Avenue/Nashville, TN 37203',
    '314 Chattanooga': '2100 Hamilton Place Boulevard Suite 318/Chattanooga, TN 37421',
    '315 Johnson City': '2011 North Roan Street/Johnson City, TN 37601',
    '316 Louisville': '3702 Lexington Rd/Louisville, KY 40207',
    '317 Asheville': '8 Town Square Blvd #130/Asheville, NC 28803',
    '401 Idaho Falls': '2980 South 25th East/Idaho Falls, ID 83404',
    '404 Missoula': '2901 Brooks Street D-2/Missoula, MT 59801',
    '406 Bozeman': '2825 W. Main St. Unit #5-6B/Bozeman, MT 59718',
    '410 Bend': '330 SW Powerhouse Dr. Suite #120/Bend, OR 97702',
    '415 Portland': '700 NE Multnomah Street Ste 190/Portland, OR 97232',
    '419 Corvallis': '140C NW 3rd St./Corvallis, OR 97330',
    '420 Eugene': '881 E 13th Ave/Eugene, OR 97401',
    '421 Hillsboro': '2165 NE Allie Ave Space 550/Hillsboro, OR 97124',
    '510 Springfield': '2714 South Glenstone Ave/Springfield, MO 65804',
    #'511 Lawrence': '3221 Iowa Street/Lawrence, KS 66046',
    '514 Columbia MO': '2703 E Broadway, Suite 220/Columbia, MO 65201',
    #'602 Columbia SC': '4840 Forest Drive, Suite 6-B/Columbia, SC 29206',
    #'603 Wilmington': '6835 Conservation Way, Space J115/Wilmington, NC 28405',
    #'604 Myrtle Beach': '130 SayeBrook Parkway, Unit 1/Myrtle Beach, SC 29588',
    '605 Winston Salem': '276 S Stratford Rd/Winston Salem, NC 27103',
    '702 Athens': '1850 Epps Bridge Pkwy Suite 207/Athens, GA 30606',
    '704 Charlottesville': '1111 Emmet Street North/Charlottesville, VA 22903',
    '705 Macon': '5005 Riverside Drive, Suite B/Macon, GA 31210',
    '706 West Cobb': '3625 Dallas Hwy Suite 765/Marietta, GA 30064',
    '707 Peachtree City': '304 City Circle Suite 1500A/Peachtree City, GA 30269',
    '708 Norcross': '5171 Peachtree Pkwy Suite 505/Peachtree Corners, GA 30092',
    '710 Forsyth': '410 Peachtree Pkwy Suite 4142/Cumming, GA 30041',
    '711 East Cobb': '4475 Roswell Rd Suite 420/Marietta, GA 30062',
    '712 Montgomery': '7070 Eastchase Parkway/Montgomery, AL 36117',
    '713 St. Simons': '26 Market Street Suite 116/St. Simons Island, GA 31522',
    '714 Orlando': '4953 International Drive Store #1B.10/Orlando, FL 32819',
    '715 Sawgrass': '12801 W Sunrise Blvd, Suite#243/Sunrise, FL 33323',
    '716 Dolphin': '11401 NW 12th Street, Suite# E-296/Miami, FL 33172',
    '717 Gainesville': '1122 Dawsonville Highway, Unit No. 8/Gainesville, GA 30501',
    '801 Destin': '4344 Legendary Drive, Space: B-112/Destin, FL 32541',
    '802 Tallahassee': '699 W Gaines Street, Unit 102/Tallahassee, FL 32304',
    #'803 Tuscaloosa': '1320 McFarland Blvd E, Space #260/Tuscaloosa, AL 35404',
    '805 Orlando UCF': '12101 University Boulevard, Suite 237/Orlando, FL 32817'
}
# End store dictionary


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', store_dict=store_dict.items())


# Create instructions tab and tell it to pull the form values
@app.route('/instructions', methods=['POST', 'GET'])
def instructions():
    if request.method == 'POST':
        name = request.form['name']
        title = request.form['title']
        phone = request.form['phone']
        email = request.form['email']
        cell = request.form['cell']
        cell_len = len(cell)
        return render_template('instructions.html', name=name, title=title, phone=phone, cell=cell, email=email,
                               cell_len=cell_len)
    else:
        return redirect(url_for('home'))


@app.route('/RetailInstructions', methods=['POST', 'GET'])
def instructions2():
    if request.method == 'POST':
        name = request.form['name']
        title = request.form['title']
        phone = request.form['phone']
        email = request.form['email']
        store = request.form['storeDropDown']

        storeValueString = store_dict.get(store)
        storeValueList = storeValueString.rsplit('/', 1)

        return render_template('instructions2.html', name=name, title=title, phone=phone, email=email,
                               store=store, store_dict=store_dict, storeValueList=storeValueList)
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
