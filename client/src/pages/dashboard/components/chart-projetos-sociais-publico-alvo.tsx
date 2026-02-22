import { Pie, PieChart, Cell } from "recharts";
import { useMemo } from "react";

import {
    Card,
    CardContent,
    CardDescription,
    CardHeader,
    CardTitle,
} from "@/components/ui/card";
import {
    ChartConfig,
    ChartContainer,
    ChartLegend,
    ChartLegendContent,
    ChartTooltip,
    ChartTooltipContent,
} from "@/components/ui/chart";
import Text from "@/components/commons/text";

type Props = {
    chartData: {
        label: string
        total: number
    }[]
}

const normalizeKey = (value: string) =>
    value
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .toLowerCase()

export default function ChartProjetosSociaisPublicoAlvo({ chartData }: Props) {
    const normalizedData = chartData.map(item => {
        const key = normalizeKey(item.label)

        return {
            ...item,
            tipoKey: key,
        }
    })

    const colors = useMemo(() => {
        return chartData.map(() => {
            const h = Math.floor(Math.random() * 360)
            return `hsl(${h}, 70%, 50%)`
        })
    }, [chartData])

    const chartConfig = useMemo(() => {
        const cfg: Record<string, { label: string; color: string }> = {}

        normalizedData.forEach((d, i) => {
            cfg[d.tipoKey] = { label: d.label, color: colors[i] }
        })

        return cfg as ChartConfig
    }, [normalizedData, colors])

    return (
        <Card className="flex flex-col h-full">
            <CardHeader className="pb-0">
                <CardTitle>Projetos Sociais por Público Alvo</CardTitle>
                <CardDescription>
                    Total de projetos sociais por público alvo  
                </CardDescription>
            </CardHeader>

            <CardContent className="flex-1 pb-0">
                <ChartContainer
                    config={chartConfig}
                    className="mx-auto aspect-square"
                >
                    {!chartData.length ? (
                        <div className="flex h-full w-full items-center justify-center">
                            <Text className="text-muted-foreground">
                                Nenhum registro encontrado.
                            </Text>
                        </div>
                    ) : (
                        <PieChart>
                            <ChartTooltip content={<ChartTooltipContent hideLabel />} />

                            <Pie
                                data={normalizedData}
                                dataKey="total"
                                nameKey="tipoKey"
                                cx="50%"
                                cy="50%"
                                innerRadius="50%"
                                outerRadius="80%"
                                paddingAngle={4}
                                label={false}
                            >
                                {normalizedData.map((_, i) => (
                                    <Cell key={`cell-${i}`} fill={colors[i]} />
                                ))}
                            </Pie>

                            <ChartLegend
                                content={<ChartLegendContent nameKey="tipoKey" />}
                                className="-translate-y-2 flex-wrap gap-2 [&>*]:basis-1/4 [&>*]:justify-center"
                            />
                        </PieChart>
                    )}
                </ChartContainer>
            </CardContent>
        </Card>
    )
}

