<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class ServletContext implements \JsonSerializable
{
    /**
     * @var int|null
     */
    private $majorVersion;

    /**
     * @var int|null
     */
    private $minorVersion;

    /**
     * @var ClassLoader|null
     */
    private $classLoader;

    /**
     * @var array|null
     */
    private $servletNames;

    /**
     * @var array|null
     */
    private $attributeNames;

    /**
     * @var string|null
     */
    private $contextPath;

    /**
     * @var int|null
     */
    private $sessionTimeout;

    /**
     * @var string|null
     */
    private $servletContextName;

    /**
     * @var string|null
     */
    private $serverInfo;

    /**
     * @var array|null
     */
    private $initParameterNames;

    /**
     * @var string|null
     */
    private $requestCharacterEncoding;

    /**
     * @var string|null
     */
    private $responseCharacterEncoding;

    /**
     * @var array|null
     */
    private $servlets;

    /**
     * @var SessionCookieConfig|null
     */
    private $sessionCookieConfig;

    /**
     * @var array<string,ServletRegistration>|null
     */
    private $servletRegistrations;

    /**
     * @var array<string,FilterRegistration>|null
     */
    private $filterRegistrations;

    /**
     * @var string[]|null
     */
    private $defaultSessionTrackingModes;

    /**
     * @var string[]|null
     */
    private $effectiveSessionTrackingModes;

    /**
     * @var JspConfigDescriptor|null
     */
    private $jspConfigDescriptor;

    /**
     * @var string|null
     */
    private $virtualServerName;

    /**
     * @var int|null
     */
    private $effectiveMajorVersion;

    /**
     * @var int|null
     */
    private $effectiveMinorVersion;

    /**
     * Returns Major Version.
     */
    public function getMajorVersion(): ?int
    {
        return $this->majorVersion;
    }

    /**
     * Sets Major Version.
     *
     * @maps majorVersion
     */
    public function setMajorVersion(?int $majorVersion): void
    {
        $this->majorVersion = $majorVersion;
    }

    /**
     * Returns Minor Version.
     */
    public function getMinorVersion(): ?int
    {
        return $this->minorVersion;
    }

    /**
     * Sets Minor Version.
     *
     * @maps minorVersion
     */
    public function setMinorVersion(?int $minorVersion): void
    {
        $this->minorVersion = $minorVersion;
    }

    /**
     * Returns Class Loader.
     */
    public function getClassLoader(): ?ClassLoader
    {
        return $this->classLoader;
    }

    /**
     * Sets Class Loader.
     *
     * @maps classLoader
     */
    public function setClassLoader(?ClassLoader $classLoader): void
    {
        $this->classLoader = $classLoader;
    }

    /**
     * Returns Servlet Names.
     */
    public function getServletNames(): ?array
    {
        return $this->servletNames;
    }

    /**
     * Sets Servlet Names.
     *
     * @maps servletNames
     */
    public function setServletNames(?array $servletNames): void
    {
        $this->servletNames = $servletNames;
    }

    /**
     * Returns Attribute Names.
     */
    public function getAttributeNames(): ?array
    {
        return $this->attributeNames;
    }

    /**
     * Sets Attribute Names.
     *
     * @maps attributeNames
     */
    public function setAttributeNames(?array $attributeNames): void
    {
        $this->attributeNames = $attributeNames;
    }

    /**
     * Returns Context Path.
     */
    public function getContextPath(): ?string
    {
        return $this->contextPath;
    }

    /**
     * Sets Context Path.
     *
     * @maps contextPath
     */
    public function setContextPath(?string $contextPath): void
    {
        $this->contextPath = $contextPath;
    }

    /**
     * Returns Session Timeout.
     */
    public function getSessionTimeout(): ?int
    {
        return $this->sessionTimeout;
    }

    /**
     * Sets Session Timeout.
     *
     * @maps sessionTimeout
     */
    public function setSessionTimeout(?int $sessionTimeout): void
    {
        $this->sessionTimeout = $sessionTimeout;
    }

    /**
     * Returns Servlet Context Name.
     */
    public function getServletContextName(): ?string
    {
        return $this->servletContextName;
    }

    /**
     * Sets Servlet Context Name.
     *
     * @maps servletContextName
     */
    public function setServletContextName(?string $servletContextName): void
    {
        $this->servletContextName = $servletContextName;
    }

    /**
     * Returns Server Info.
     */
    public function getServerInfo(): ?string
    {
        return $this->serverInfo;
    }

    /**
     * Sets Server Info.
     *
     * @maps serverInfo
     */
    public function setServerInfo(?string $serverInfo): void
    {
        $this->serverInfo = $serverInfo;
    }

    /**
     * Returns Init Parameter Names.
     */
    public function getInitParameterNames(): ?array
    {
        return $this->initParameterNames;
    }

    /**
     * Sets Init Parameter Names.
     *
     * @maps initParameterNames
     */
    public function setInitParameterNames(?array $initParameterNames): void
    {
        $this->initParameterNames = $initParameterNames;
    }

    /**
     * Returns Request Character Encoding.
     */
    public function getRequestCharacterEncoding(): ?string
    {
        return $this->requestCharacterEncoding;
    }

    /**
     * Sets Request Character Encoding.
     *
     * @maps requestCharacterEncoding
     */
    public function setRequestCharacterEncoding(?string $requestCharacterEncoding): void
    {
        $this->requestCharacterEncoding = $requestCharacterEncoding;
    }

    /**
     * Returns Response Character Encoding.
     */
    public function getResponseCharacterEncoding(): ?string
    {
        return $this->responseCharacterEncoding;
    }

    /**
     * Sets Response Character Encoding.
     *
     * @maps responseCharacterEncoding
     */
    public function setResponseCharacterEncoding(?string $responseCharacterEncoding): void
    {
        $this->responseCharacterEncoding = $responseCharacterEncoding;
    }

    /**
     * Returns Servlets.
     */
    public function getServlets(): ?array
    {
        return $this->servlets;
    }

    /**
     * Sets Servlets.
     *
     * @maps servlets
     */
    public function setServlets(?array $servlets): void
    {
        $this->servlets = $servlets;
    }

    /**
     * Returns Session Cookie Config.
     */
    public function getSessionCookieConfig(): ?SessionCookieConfig
    {
        return $this->sessionCookieConfig;
    }

    /**
     * Sets Session Cookie Config.
     *
     * @maps sessionCookieConfig
     */
    public function setSessionCookieConfig(?SessionCookieConfig $sessionCookieConfig): void
    {
        $this->sessionCookieConfig = $sessionCookieConfig;
    }

    /**
     * Returns Servlet Registrations.
     *
     * @return array<string,ServletRegistration>|null
     */
    public function getServletRegistrations(): ?array
    {
        return $this->servletRegistrations;
    }

    /**
     * Sets Servlet Registrations.
     *
     * @maps servletRegistrations
     *
     * @param array<string,ServletRegistration>|null $servletRegistrations
     */
    public function setServletRegistrations(?array $servletRegistrations): void
    {
        $this->servletRegistrations = $servletRegistrations;
    }

    /**
     * Returns Filter Registrations.
     *
     * @return array<string,FilterRegistration>|null
     */
    public function getFilterRegistrations(): ?array
    {
        return $this->filterRegistrations;
    }

    /**
     * Sets Filter Registrations.
     *
     * @maps filterRegistrations
     *
     * @param array<string,FilterRegistration>|null $filterRegistrations
     */
    public function setFilterRegistrations(?array $filterRegistrations): void
    {
        $this->filterRegistrations = $filterRegistrations;
    }

    /**
     * Returns Default Session Tracking Modes.
     *
     * @return string[]|null
     */
    public function getDefaultSessionTrackingModes(): ?array
    {
        return $this->defaultSessionTrackingModes;
    }

    /**
     * Sets Default Session Tracking Modes.
     *
     * @maps defaultSessionTrackingModes
     * @factory \SwaggerScarecrowLib\Models\DefaultSessionTrackingModeEnum::checkValue
     *
     * @param string[]|null $defaultSessionTrackingModes
     */
    public function setDefaultSessionTrackingModes(?array $defaultSessionTrackingModes): void
    {
        $this->defaultSessionTrackingModes = $defaultSessionTrackingModes;
    }

    /**
     * Returns Effective Session Tracking Modes.
     *
     * @return string[]|null
     */
    public function getEffectiveSessionTrackingModes(): ?array
    {
        return $this->effectiveSessionTrackingModes;
    }

    /**
     * Sets Effective Session Tracking Modes.
     *
     * @maps effectiveSessionTrackingModes
     * @factory \SwaggerScarecrowLib\Models\EffectiveSessionTrackingModeEnum::checkValue
     *
     * @param string[]|null $effectiveSessionTrackingModes
     */
    public function setEffectiveSessionTrackingModes(?array $effectiveSessionTrackingModes): void
    {
        $this->effectiveSessionTrackingModes = $effectiveSessionTrackingModes;
    }

    /**
     * Returns Jsp Config Descriptor.
     */
    public function getJspConfigDescriptor(): ?JspConfigDescriptor
    {
        return $this->jspConfigDescriptor;
    }

    /**
     * Sets Jsp Config Descriptor.
     *
     * @maps jspConfigDescriptor
     */
    public function setJspConfigDescriptor(?JspConfigDescriptor $jspConfigDescriptor): void
    {
        $this->jspConfigDescriptor = $jspConfigDescriptor;
    }

    /**
     * Returns Virtual Server Name.
     */
    public function getVirtualServerName(): ?string
    {
        return $this->virtualServerName;
    }

    /**
     * Sets Virtual Server Name.
     *
     * @maps virtualServerName
     */
    public function setVirtualServerName(?string $virtualServerName): void
    {
        $this->virtualServerName = $virtualServerName;
    }

    /**
     * Returns Effective Major Version.
     */
    public function getEffectiveMajorVersion(): ?int
    {
        return $this->effectiveMajorVersion;
    }

    /**
     * Sets Effective Major Version.
     *
     * @maps effectiveMajorVersion
     */
    public function setEffectiveMajorVersion(?int $effectiveMajorVersion): void
    {
        $this->effectiveMajorVersion = $effectiveMajorVersion;
    }

    /**
     * Returns Effective Minor Version.
     */
    public function getEffectiveMinorVersion(): ?int
    {
        return $this->effectiveMinorVersion;
    }

    /**
     * Sets Effective Minor Version.
     *
     * @maps effectiveMinorVersion
     */
    public function setEffectiveMinorVersion(?int $effectiveMinorVersion): void
    {
        $this->effectiveMinorVersion = $effectiveMinorVersion;
    }

    /**
     * Encode this object to JSON
     *
     * @param bool $asArrayWhenEmpty Whether to serialize this model as an array whenever no fields
     *        are set. (default: false)
     *
     * @return array|stdClass
     */
    #[\ReturnTypeWillChange] // @phan-suppress-current-line PhanUndeclaredClassAttribute for (php < 8.1)
    public function jsonSerialize(bool $asArrayWhenEmpty = false)
    {
        $json = [];
        if (isset($this->majorVersion)) {
            $json['majorVersion']                  = $this->majorVersion;
        }
        if (isset($this->minorVersion)) {
            $json['minorVersion']                  = $this->minorVersion;
        }
        if (isset($this->classLoader)) {
            $json['classLoader']                   = $this->classLoader;
        }
        if (isset($this->servletNames)) {
            $json['servletNames']                  = $this->servletNames;
        }
        if (isset($this->attributeNames)) {
            $json['attributeNames']                = $this->attributeNames;
        }
        if (isset($this->contextPath)) {
            $json['contextPath']                   = $this->contextPath;
        }
        if (isset($this->sessionTimeout)) {
            $json['sessionTimeout']                = $this->sessionTimeout;
        }
        if (isset($this->servletContextName)) {
            $json['servletContextName']            = $this->servletContextName;
        }
        if (isset($this->serverInfo)) {
            $json['serverInfo']                    = $this->serverInfo;
        }
        if (isset($this->initParameterNames)) {
            $json['initParameterNames']            = $this->initParameterNames;
        }
        if (isset($this->requestCharacterEncoding)) {
            $json['requestCharacterEncoding']      = $this->requestCharacterEncoding;
        }
        if (isset($this->responseCharacterEncoding)) {
            $json['responseCharacterEncoding']     = $this->responseCharacterEncoding;
        }
        if (isset($this->servlets)) {
            $json['servlets']                      = $this->servlets;
        }
        if (isset($this->sessionCookieConfig)) {
            $json['sessionCookieConfig']           = $this->sessionCookieConfig;
        }
        if (isset($this->servletRegistrations)) {
            $json['servletRegistrations']          = $this->servletRegistrations;
        }
        if (isset($this->filterRegistrations)) {
            $json['filterRegistrations']           = $this->filterRegistrations;
        }
        if (isset($this->defaultSessionTrackingModes)) {
            $json['defaultSessionTrackingModes']   =
                DefaultSessionTrackingModeEnum::checkValue(
                    $this->defaultSessionTrackingModes
                );
        }
        if (isset($this->effectiveSessionTrackingModes)) {
            $json['effectiveSessionTrackingModes'] =
                EffectiveSessionTrackingModeEnum::checkValue(
                    $this->effectiveSessionTrackingModes
                );
        }
        if (isset($this->jspConfigDescriptor)) {
            $json['jspConfigDescriptor']           = $this->jspConfigDescriptor;
        }
        if (isset($this->virtualServerName)) {
            $json['virtualServerName']             = $this->virtualServerName;
        }
        if (isset($this->effectiveMajorVersion)) {
            $json['effectiveMajorVersion']         = $this->effectiveMajorVersion;
        }
        if (isset($this->effectiveMinorVersion)) {
            $json['effectiveMinorVersion']         = $this->effectiveMinorVersion;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
