# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    cpv = fields.Char(
        string="CPV",
        help="Cash Payment Voucher reference for this payment.",
    )
    check_no = fields.Char(
        string="Check No.",
        help="Check number for this payment.",
    )

    def _create_payment_vals_from_wizard(self, batch_result):
        payment_vals = super()._create_payment_vals_from_wizard(batch_result)
        payment_vals.update(
            {
                "cpv": self.cpv.strip() if self.cpv else False,
                "check_no": self.check_no.strip() if self.check_no else False,
            }
        )
        return payment_vals


class AccountPayment(models.Model):
    _inherit = "account.payment"

    cpv = fields.Char(
        string="CPV",
        help="Cash Payment Voucher reference for this payment.",
        copy=False,
    )
    check_no = fields.Char(
        string="Check No.",
        help="Check number for this payment.",
        copy=False,
    )

