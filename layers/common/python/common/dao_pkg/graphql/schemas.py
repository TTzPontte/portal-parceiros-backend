schemas = {
    "UserInvite": {
        "get":  """query getUserInvite($id: ID!) {
                    getUserInvite(id: $id) {
                        authType
                        createdAt
                        guestId
                        hostId
                        id
                        owner
                        status
                        organizationId
                        updatedAt
                        _lastChangedAt
                        _version
                        _deleted
                    }
                  }
                """,
        "create": """mutation createUserInvite($input: CreateUserInviteInput!) {
                      createUserInvite(input: $input) {
                        authType
                        guestId
                        createdAt
                        _version
                        _lastChangedAt
                        _deleted
                        updatedAt
                        status
                        owner
                        organizationId
                        id
                        hostId
                    }
                  """,
        "update": """mutation updateUserInvite($input: UpdateUserInviteInput!) {
                      updateUserInvite(input: $input) {
                        authType
                        guestId
                        createdAt
                        _version
                        _lastChangedAt
                        _deleted
                        updatedAt
                        status
                        owner
                        organizationId
                        id
                        hostId
                      }
                    }
                """,
        "delete": """mutation MyMutation($input: DeleteUserInviteInput!) {
                      deleteUserInvite(input: $input) {
                        authType
                        guestId
                        createdAt
                        _version
                        _lastChangedAt
                        _deleted
                        updatedAt
                        status
                        owner
                        organizationId
                        id
                        hostId
                      }
                    }
                """
    },
    "Organization": {
        "get": """query getOrganization($id: ID!) {
                  getOrganization(id: $id) {
                    _deleted
                    _lastChangedAt
                    _version
                    documentNumber
                    createdAt
                    id
                    image
                    name
                    legalName
                    owner
                    phone
                    pipefyId
                    updatedAt
                  }
                }  
              """,
        "create": """mutation createOrganization($input: CreateOrganizationInput!) {
                      createOrganization(input: $input) {
                        _deleted
                        _lastChangedAt
                        _version
                        documentNumber
                        createdAt
                        id
                        image
                        name
                        legalName
                        owner
                        phone
                        pipefyId
                        updatedAt
                      }
                    }
                  """,
        "update": """mutation updateOrganization($input: UpdateOrganizationInput!) {
                      updateOrganization(input: $input) {
                        _deleted
                        _lastChangedAt
                        _version
                        documentNumber
                        createdAt
                        id
                        image
                        name
                        legalName
                        owner
                        phone
                        pipefyId
                        updatedAt
                      }
                    }""",
        "delete": """mutation deleteOrganization($input: DeleteOrganizationInput!) {
                    deleteOrganization(input: $input) {
                      _deleted
                      _lastChangedAt
                      _version
                      documentNumber
                      createdAt
                      id
                      image
                      name
                      legalName
                      owner
                      phone
                      pipefyId
                      updatedAt
                    }
                  }
                """
    },
    "Lead": {
        "get": """query getLead($id: ID!) {
                getLead(id: $id) {
                  _deleted
                  _lastChangedAt
                  _version
                  documentNumber
                  email
                  id
                  leadSimulationId
                  name
                  memberId
                  organizationId
                  owner
                  phone
                  pipefyId
                  status
                  type
                  updatedAt
                  value
                }
              }""",
        "create": """mutation createLead($input: CreateLeadInput!) {
                    createLead(input: $input) {
                      _deleted
                      _lastChangedAt
                      _version
                      documentNumber
                      email
                      id
                      leadSimulationId
                      name
                      memberId
                      organizationId
                      owner
                      phone
                      pipefyId
                      status
                      type
                      updatedAt
                      value
                    }
                  }""",
        "update": """mutation updateLead($input: UpdateLeadInput!) {
                  updateLead(input: $input) {
                    _deleted
                    _lastChangedAt
                    _version
                    documentNumber
                    email
                    id
                    leadSimulationId
                    name
                    memberId
                    organizationId
                    owner
                    phone
                    pipefyId
                    status
                    type
                    updatedAt
                    value
                  }
                }""",
        "delete": """mutation deleteLead($input: DeleteLeadInput!) {
                    deleteLead(input: $input) {
                      _deleted
                      _lastChangedAt
                      _version
                      documentNumber
                      email
                      id
                      leadSimulationId
                      name
                      memberId
                      organizationId
                      owner
                      phone
                      pipefyId
                      status
                      type
                      updatedAt
                      value
                    }
                  }"""
    },
    "Member": {
        "get": """query getMember($id: ID!) {
                  getMember(id: $id) {
                    _deleted
                    _lastChangedAt
                    _version
                    welcome
                    userId
                    updatedAt
                    phone
                    owner
                    organizationId
                    name
                    id
                    email
                    documentNumber
                    createdAt
                    avatar
                    birthDate
                  }
                }
                """,
        "create": """mutation createMember($input: CreateMemberInput!) {
                      createMember(input: $input) {
                      _deleted
                      _lastChangedAt
                      _version
                      welcome
                      userId
                      updatedAt
                      phone
                      owner
                      organizationId
                      name
                      id
                      email
                      documentNumber
                      createdAt
                      avatar
                      birthDate
                      }
                    }""",
        "update": """mutation updateMember($input: UpdateMemberInput!) {
                    updateMember(input: $input) {
                      _deleted
                      _lastChangedAt
                      _version
                      welcome
                      userId
                      updatedAt
                      phone
                      owner
                      organizationId
                      name
                      id
                      email
                      documentNumber
                      createdAt
                      avatar
                      birthDate
                    }
                  }""",
        "delete": """mutation deleteMember($input: DeleteMemberInput!) {
                deleteMember(input: $input) {
                    _deleted
                    _lastChangedAt
                    _version
                    welcome
                    userId
                    updatedAt
                    phone
                    owner
                    organizationId
                    name
                    id
                    email
                    documentNumber
                    createdAt
                    avatar
                    birthDate
                }
              }"""
    },
    "Simulation": {
        "get": """query getSimulation($id: ID!) {
                  getSimulation(id: $id) {
                    _deleted
                    _lastChangedAt
                    _version
                    createdAt
                    dayDue
                    entranceValue
                    gracePeriod
                    itbi
                    id
                    legalPerson
                    linkPDFSimulation
                    memberId
                    loanValue
                    loanDate
                    skipMonth
                    propertyValue
                    owner
                    organizationId
                    monthlyIncome
                    updatedAt
                    type
                    term
                    table
                  }
                }
                """,
        "create": """mutation createSimulation($input: CreateSimulationInput!) {
                    createSimulation (input: $input){
                      _deleted
                      _lastChangedAt
                      _version
                      createdAt
                      dayDue
                      entranceValue
                      gracePeriod
                      itbi
                      id
                      legalPerson
                      linkPDFSimulation
                      memberId
                      loanValue
                      loanDate
                      skipMonth
                      propertyValue
                      owner
                      organizationId
                      monthlyIncome
                      updatedAt
                      type
                      term
                      table
                    }
                  }""",
        "update": """mutation updateSimulation($input: UpdateSimulationInput!) {
                    updateSimulation(input: $input) {
                      _deleted
                      _lastChangedAt
                      _version
                      createdAt
                      dayDue
                      entranceValue
                      gracePeriod
                      itbi
                      id
                      legalPerson
                      linkPDFSimulation
                      memberId
                      loanValue
                      loanDate
                      skipMonth
                      propertyValue
                      owner
                      organizationId
                      monthlyIncome
                      updatedAt
                      type
                      term
                      table
                    }
                  }""",
        "delete": """mutation deleteSimulation($input: DeleteSimulationInput!) {
                      deleteSimulation(input: $input) {
                        _deleted
                        _lastChangedAt
                        _version
                        createdAt
                        dayDue
                        entranceValue
                        gracePeriod
                        itbi
                        id
                        legalPerson
                        linkPDFSimulation
                        memberId
                        loanValue
                        loanDate
                        skipMonth
                        propertyValue
                        owner
                        organizationId
                        monthlyIncome
                        updatedAt
                        type
                        term
                        table
                      }
                    }"""
    },
    "WhiteLabel": {
        "get": """query getWhiteLabel($id: ID!) {
                        getWhiteLabel(id: $id) {
                            _deleted
                            _lastChangedAt
                            _version
                            active
                            background
                            createdAt
                            id
                            logo
                            owner
                            partnerName
                            path
                            primary
                            secondary
                            tertiary
                            type
                            updatedAt
                            whiteLabelOrganizationId
                        }
                      }
                """,
        "list": """
          query listWhiteLabels {
                  listWhiteLabels {
                    items {
                        _deleted
                        _lastChangedAt
                        _version
                        active
                        background
                        createdAt
                        id
                        logo
                        owner
                        partnerName
                        path
                        primary
                        secondary
                        tertiary
                        type
                        updatedAt
                        whiteLabelOrganizationId
                    }
                  }
                }
        """,
        "create": """mutation CreateWhiteLabel($input: CreateWhiteLabelInput!) {
                      createWhiteLabel(input: $input) {
                            _deleted
                            _lastChangedAt
                            _version
                            active
                            background
                            createdAt
                            id
                            logo
                            owner
                            partnerName
                            path
                            primary
                            secondary
                            tertiary
                            type
                            updatedAt
                            whiteLabelOrganizationId
                      }
                    }
                    """,
        "update": """mutation MyMutation($input: UpdateWhiteLabelInput!) {
                updateWhiteLabel(input: $input) {
                            _deleted
                            _lastChangedAt
                            _version
                            active
                            background
                            createdAt
                            id
                            logo
                            owner
                            partnerName
                            path
                            primary
                            secondary
                            tertiary
                            type
                            updatedAt
                            whiteLabelOrganizationId
                }
              }""",
        "delete": """mutation MyMutation($input: DeleteWhiteLabelInput!) {
                    deleteWhiteLabel(input: $input){
                            _deleted
                            _lastChangedAt
                            _version
                            active
                            background
                            createdAt
                            id
                            logo
                            owner
                            partnerName
                            path
                            primary
                            secondary
                            tertiary
                            type
                            updatedAt
                            whiteLabelOrganizationId
                    }
                  }
                """
    },
    "User": {
        "get": """
            query GetUser($id: ID!) {
                  getUser(id: $id) {
                    _deleted
                    _lastChangedAt
                    _version
                    createdAt
                    email
                    id
                    name
                    updatedAt
                    welcome
                  }
                }
        """,
        "create": """
            mutation CreateUser($input: CreateUserInput!) {
                  createUser(input: $input) {
                    _deleted
                    _lastChangedAt
                    _version
                    createdAt
                    email
                    id
                    name
                    updatedAt
                    welcome
                  }
                }
        """,
        "update": """
            mutation UpdateUser($input: UpdateUserInput!) {
              updateUser(input: $input) {
                welcome
                updatedAt
                name
                id
                email
                createdAt
                _version
                _lastChangedAt
                _deleted
              }
            }
        """,
        "delete": """
            mutation DeleteUser($input: DeleteUserInput!) {
              deleteUser(input: $input) {
                welcome
                updatedAt
                name
                id
                email
                createdAt
                _version
                _lastChangedAt
                _deleted
              }
            }
        """
    }
}
