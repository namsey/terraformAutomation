def get_service_prompt():
    """Prompt the user to enter the AWS service they want."""
    return input("Enter the AWS service (e.g., EC2, VPC, S3, EKS, etc.): ")


def get_region_prompt():
    """Prompt the user to enter the desired AWS region."""
    return input("Enter the desired AWS region (e.g., us-east-1, us-west-2, etc.): ")


def get_additional_details_prompt():
    """Prompt the user to enter any additional details."""
    return input("Enter any additional details: ")


def get_combined_prompt():
    """Combine all prompts into a single prompt for the model."""
    service = get_service_prompt()
    region = get_region_prompt()
    additional_details = get_additional_details_prompt()

    return f"create terraform code for {service} in {region}. {additional_details}"
