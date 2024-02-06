from pyDICOS import (
    AuthenticationCallbackConnectsSpecificClientApps,
    DataProcessingConnectsSpecificClientApps,
    DcsApplicationEntity,
    DcsServer,
    IDcsServer,
)


def main():
    datacallback = DataProcessingConnectsSpecificClientApps()
    authenticationcallback = AuthenticationCallbackConnectsSpecificClientApps()
    server = DcsServer()
    server.SetPort(1000)
    server.SetApplicationName(DcsApplicationEntity("ServerExample"))

    server.RequireApplicationNames()

    server.DisableDataCompression()
    server.PrioritizeDataCompression(False)

    if server.StartListening(
            datacallback,
            authenticationcallback,
            IDcsServer.RETRIEVE_METHOD.enumMethodUserAPI,
            False,
        ):
        print(
            "Failed to start DICOS server. IP:Port: ",
            server.GetIP(),
            ":",
            server.GetPort(),
        )
        return 1

    input("Press enter to stop server...")
    server.StopListening()
    return 0


if __name__ == "__main__":
    main()
