from django_stripe.account.models import Account
from django_stripe.charge.models import Charge
from django_stripe.checkout_session.models import CheckoutSession
from django_stripe.payment_intent.models import PaymentIntent


webhook_event_mapper = {
    "account.application.authorized": None,  # Application
    "account.application.deauthorized": None,  # Application
    "account.external_account.created": None,  # External account (e.g., card or bank account)
    "account.external_account.deleted": None,  # External account (e.g., card or bank account)
    "account.external_account.updated": None,  # External account (e.g., card or bank account)
    "account.updated": Account,
    "application_fee.created": None,  # Application fee
    "application_fee.refund.updated": None,  # Fee refund
    "application_fee.refunded": None,  # Application fee
    "balance.available": None,  # Balance
    "billing_portal.configuration.created": None,  # Billing portal configuration
    "billing_portal.configuration.updated": None,  # Billing portal configuration
    "billing_portal.session.created": None,  # Billing portal session
    "capability.updated": None,  # Capability
    "cash_balance.funds_available": None,  # Cash balance
    "charge.captured": Charge,
    "charge.dispute.closed": None,  # Dispute
    "charge.dispute.created": None,  # Dispute
    "charge.dispute.funds_reinstated": None,  # Dispute
    "charge.dispute.funds_withdrawn": None,  # Dispute
    "charge.dispute.updated": None,  # Dispute
    "charge.expired": Charge,
    "charge.failed": Charge,
    "charge.pending": Charge,
    "charge.refund.updated": None,  # Refund
    "charge.refunded": Charge,
    "charge.succeeded": Charge,
    "charge.updated": Charge,
    "checkout.session.async_payment_failed": CheckoutSession,
    "checkout.session.async_payment_succeeded": CheckoutSession,
    "checkout.session.completed": CheckoutSession,
    "checkout.session.expired": CheckoutSession,
    "climate.order.canceled": None,  # Climate order
    "climate.order.created": None,  # Climate order
    "climate.order.delayed": None,  # Climate order
    "climate.order.delivered": None,  # Climate order
    "climate.order.product_substituted": None,  # Climate order
    "climate.product.created": None,  # Climate product
    "climate.product.pricing_updated": None,  # Climate product
    "coupon.created": None,  # Coupon
    "coupon.deleted": None,  # Coupon
    "coupon.updated": None,  # Coupon
    "credit_note.created": None,  # Credit note
    "credit_note.updated": None,  # Credit note
    "credit_note.voided": None,  # Credit note
    "customer_cash_balance_transaction.created": None,  # Customer cash balance transaction
    "customer.created": None,  # Customer
    "customer.deleted": None,  # Customer
    "customer.discount.created": None,  # Discount
    "customer.discount.deleted": None,  # Discount
    "customer.discount.updated": None,  # Discount
    "customer.source.created": None,  # Source (e.g., card)
    "customer.source.deleted": None,  # Source (e.g., card)
    "customer.source.expiring": None,  # Source (e.g., card)
    "customer.source.updated": None,  # Source (e.g., card)
    "customer.subscription.created": None,  # Subscription
    "customer.subscription.deleted": None,  # Subscription
    "customer.subscription.paused": None,  # Subscription
    "customer.subscription.pending_update_applied": None,  # Subscription
    "customer.subscription.pending_update_expired": None,  # Subscription
    "customer.subscription.resumed": None,  # Subscription
    "customer.subscription.trial_will_end": None,  # Subscription
    "customer.subscription.updated": None,  # Subscription
    "customer.tax_id.created": None,  # Tax id
    "customer.tax_id.deleted": None,  # Tax id
    "customer.tax_id.updated": None,  # Tax id
    "customer.updated": None,  # Customer
    "entitlements.active_entitlement_summary.updated": None,  # Entitlements active entitlement summary
    "file.created": None,  # File
    "financial_connections.account.created": None,  # Financial connections account
    "financial_connections.account.deactivated": None,  # Financial connections account
    "financial_connections.account.disconnected": None,  # Financial connections account
    "financial_connections.account.reactivated": None,  # Financial connections account
    "financial_connections.account.refreshed_balance": None,  # Financial connections account
    "financial_connections.account.refreshed_ownership": None,  # Financial connections account
    "financial_connections.account.refreshed_transactions": None,  # Financial connections account
    "identity.verification_session.canceled": None,  # Identity verification session
    "identity.verification_session.created": None,  # Identity verification session
    "identity.verification_session.processing": None,  # Identity verification session
    "identity.verification_session.redacted": None,  # Identity verification sessionSelection required
    "identity.verification_session.requires_input": None,  # Identity verification session
    "identity.verification_session.verified": None,  # Identity verification session
    "invoice.created": None,  # Invoice
    "invoice.deleted": None,  # Invoice
    "invoice.finalization_failed": None,  # Invoice
    "invoice.finalized": None,  # Invoice
    "invoice.marked_uncollectible": None,  # Invoice
    "invoice.overdue": None,  # Invoice
    "invoice.paid": None,  # Invoice
    "invoice.payment_action_required": None,  # Invoice
    "invoice.payment_failed": None,  # Invoice
    "invoice.payment_succeeded": None,  # Invoice
    "invoice.sent": None,  # Invoice
    "invoice.upcoming": None,  # Invoice
    "invoice.updated": None,  # Invoice
    "invoice.voided": None,  # Invoice
    "invoice.will_be_due": None,  # Invoice
    "invoiceitem.created": None,  # Invoiceitem
    "invoiceitem.deleted": None,  # Invoiceitem
    "issuing_authorization.created": None,  # Issuing authorization
    "issuing_authorization.request": None,  # Issuing authorizationSelection required
    "issuing_authorization.updated": None,  # Issuing authorization
    "issuing_card.created": None,  # Issuing card
    "issuing_card.updated": None,  # Issuing card
    "issuing_cardholder.created": None,  # Issuing cardholder
    "issuing_cardholder.updated": None,  # Issuing cardholder
    "issuing_dispute.closed": None,  # Issuing dispute
    "issuing_dispute.created": None,  # Issuing dispute
    "issuing_dispute.funds_reinstated": None,  # Issuing dispute
    "issuing_dispute.submitted": None,  # Issuing dispute
    "issuing_dispute.updated": None,  # Issuing dispute
    "issuing_token.created": None,  # Issuing token
    "issuing_token.updated": None,  # Issuing token
    "issuing_transaction.created": None,  # Issuing transaction
    "issuing_transaction.updated": None,  # Issuing transaction
    "mandate.updated": None,  # Mandate
    "payment_intent.amount_capturable_updated": PaymentIntent,
    "payment_intent.canceled": PaymentIntent,
    "payment_intent.created": PaymentIntent,
    "payment_intent.partially_funded": PaymentIntent,
    "payment_intent.payment_failed": PaymentIntent,
    "payment_intent.processing": PaymentIntent,
    "payment_intent.requires_action": PaymentIntent,
    "payment_intent.succeeded": PaymentIntent,
    "payment_link.created": None,  # Payment link
    "payment_link.updated": None,  # Payment link
    "payment_method.attached": None,  # Payment method
    "payment_method.automatically_updated": None,  # Payment method
    "payment_method.detached": None,  # Payment method
    "payment_method.updated": None,  # Payment method
    "payout.canceled": None,  # Payout
    "payout.created": None,  # Payout
    "payout.failed": None,  # Payout
    "payout.paid": None,  # Payout
    "payout.reconciliation_completed": None,  # Payout
    "payout.updated": None,  # Payout
    "person.created": None,  # Person
    "person.deleted": None,  # Person
    "person.updated": None,  # Person
    "plan.created": None,  # Plan
    "plan.deleted": None,  # Plan
    "plan.updated": None,  # Plan
    "price.created": None,  # Price
    "price.deleted": None,  # Price
    "price.updated": None,  # Price
    "product.created": None,  # Product
    "product.deleted": None,  # Product
    "product.updated": None,  # Product
    "promotion_code.created": None,  # Promotion code
    "promotion_code.updated": None,  # Promotion code
    "quote.accepted": None,  # Quote
    "quote.canceled": None,  # Quote
    "quote.created": None,  # Quote
    "quote.finalized": None,  # Quote
    "quote.will_expire": None,  # Quote
    "radar.early_fraud_warning.created": None,  # Radar early fraud warning
    "radar.early_fraud_warning.updated": None,  # Radar early fraud warning
    "refund.created": None,  # Refund
    "refund.updated": None,  # Refund
    "reporting.report_run.failed": None,  # Reporting report run
    "reporting.report_run.succeeded": None,  # Reporting report run
    "reporting.report_type.updated": None,  # Reporting report typeSelection required
    "review.closed": None,  # Review
    "review.opened": None,  # Review
    "setup_intent.canceled": None,  # Setup intent
    "setup_intent.created": None,  # Setup intent
    "setup_intent.requires_action": None,  # Setup intent
    "setup_intent.setup_failed": None,  # Setup intent
    "setup_intent.succeeded": None,  # Setup intent
    "sigma.scheduled_query_run.created": None,  # Scheduled query run
    "source.canceled": None,  # Source (e.g., card)
    "source.chargeable": None,  # Source (e.g., card)
    "source.failed": None,  # Source (e.g., card)
    "source.mandate_notification": None,  # Source (e.g., card)
    "source.refund_attributes_required": None,  # Source (e.g., card)
    "source.transaction.created": None,  # Source transaction
    "source.transaction.updated": None,  # Source transaction
    "subscription_schedule.aborted": None,  # Subscription schedule
    "subscription_schedule.canceled": None,  # Subscription schedule
    "subscription_schedule.completed": None,  # Subscription schedule
    "subscription_schedule.created": None,  # Subscription schedule
    "subscription_schedule.expiring": None,  # Subscription schedule
    "subscription_schedule.released": None,  # Subscription schedule
    "subscription_schedule.updated": None,  # Subscription schedule
    "tax_rate.created": None,  # Tax rate
    "tax_rate.updated": None,  # Tax rate
    "tax.settings.updated": None,  # Tax settings
    "terminal.reader.action_failed": None,  # Terminal reader
    "terminal.reader.action_succeeded": None,  # Terminal reader
    "test_helpers.test_clock.advancing": None,  # Test helpers test clock
    "test_helpers.test_clock.created": None,  # Test helpers test clock
    "test_helpers.test_clock.deleted": None,  # Test helpers test clock
    "test_helpers.test_clock.internal_failure": None,  # Test helpers test clock
    "test_helpers.test_clock.ready": None,  # Test helpers test clock
    "topup.canceled": None,  # Topup
    "topup.created": None,  # Topup
    "topup.failed": None,  # Topup
    "topup.reversed": None,  # Topup
    "topup.succeeded": None,  # Topup
    "transfer.created": None,  # Transfer
    "transfer.reversed": None,  # Transfer
    "transfer.updated": None,  # Transfer
}
