from gql import gql



orderCreateFromCheckoutMutation = gql("""
mutation orderCreateFromCheckout($id: ID!, $removeCheckout: Boolean!) {
  orderCreateFromCheckout(
    id: $id
    removeCheckout: $removeCheckout
  ) {
    order {
      id
    }
    errors {
      field
      message
    }
  }
}
""")