class Customer:
    cust_ref = None
    cust_name = None
    people_cnt = None
    gender = None
    pincode = None
    mobile = None
    email = None
    nationality = None
    id_proof_type = None
    id_number = None
    cust_address = None
    db_obj = None

    def verify(self):
        self.verify_cust_ref()
        self.verify_name()
        self.verify_mobile()
        self.verify_email()
        self.verify_id_number()

    def verify_cust_ref(self):
        if self.cust_ref is None or self.cust_ref == '':
            raise Exception("Customer ref can not be empty")
        else:
            res = self.db_obj.search({'cust_ref': self.cust_ref})
            if len(res) > 0:
                raise Exception("Customer ref already present")

    def verify_name(self):
        if self.cust_name is None or self.cust_name == '':
            raise Exception("Customer name can not be empty")

    def verify_mobile(self):
        if self.mobile is not None and self.mobile != '':
            res = self.db_obj.search({'mobile': self.mobile})
            if len(res) > 0:
                raise Exception("Mobile no already present, May be belongs to another customer")

    def verify_email(self):
        if self.email is not None and self.email != '':
            res = self.db_obj.search({'email': self.email})
            if len(res) > 0:
                raise Exception("Email already present, May be belongs to another customer")

    def verify_id_number(self):
        if self.id_number is None or self.id_number == '':
            raise Exception("Customer ID no can not be empty")
        else:
            res = self.db_obj.search({'id_number': self.id_number})
            if len(res) > 0:
                raise Exception("Id no already present, May be belongs to another customer OR customer is alredy added")

    def compare_and_verify(self, cust):
        if self.cust_ref != cust.cust_ref:
            self.verify_cust_ref()

        if self.cust_name != cust.cust_name:
            self.verify_name()

        if self.mobile != cust.mobile:
            self.verify_mobile()

        if self.email != cust.email:
            self.verify_email()

        if self.id_number != cust.id_number:
            self.verify_id_number()
