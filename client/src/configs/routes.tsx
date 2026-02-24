import { createBrowserRouter, Navigate } from "react-router-dom";
import { DashboardLayout } from "@/layouts/dashboard/dashboard-layout";
import RootLayout from "@/layouts/root/root-layout";
import {
  Login,
  Dashboard,
  Campos,
  Formularios,
  FormularioDetalhes,
  ProjetosSociais,
  ProjetoSocialDetalhes,
  ProjetosSociaisEscolares,
  ProjetoSocialEscolarDetalhes,
  Error404,
  CampoDetalhes,
} from "@/pages/index";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
    children: [
      {
        path: "",
        element: <DashboardLayout />,
        children: [
          {
            index: true,
            element: <Navigate to="/dashboard" replace />,
          },
          {
            path: "dashboard",
            element: <Dashboard />,
          },
          {
            path: "projetos-sociais",
            children: [
              {
                path: "",
                element: <ProjetosSociais />,
              },
              {
                path: "incluir",
                element: <ProjetoSocialDetalhes />,
              },
              {
                path: ":id",
                element: <ProjetoSocialDetalhes />,
              },
            ],
          },
          {
            path: "cadastros",
            children: [
              {
                path: "formularios",
                children: [
                  {
                    path: "",
                    element: <Formularios />,
                  },
                  {
                    path: "incluir",
                    element: <FormularioDetalhes />,
                  },
                  {
                    path: ":id",
                    element: <FormularioDetalhes />,
                  },
                ]
              },
            ],
          },
          {
            path: "formularios",
            children: [
              {
                path: "campos",
                children: [
                  {
                    path: "",
                    element: <Campos />,
                  },
                  {
                    path: "incluir",
                    element: <CampoDetalhes />,
                  },
                  {
                    path: ":id",
                    element: <CampoDetalhes />,
                  },
                ]
              },
            ],
          },
          {
            path: "projetos-sociais-escolares",
            children: [
              {
                path: "",
                element: <ProjetosSociaisEscolares />,
              },
              {
                path: "incluir",
                element: <ProjetoSocialEscolarDetalhes />,
              },
              {
                path: ":codigo_ue/ue",
                element: <ProjetoSocialEscolarDetalhes />,
              },
            ],
          },
        ],
      },
    ],
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/*",
    element: <Error404 />,
  },
]);
